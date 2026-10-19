---
Provider: AMD
Platform: AMD AI Developer Program, AMD AI Academy
---

# 4. HIP[^1] Programming and Porting from CUDA to HIP[^1]

<span style="color: gray;">Dated: 16-10-2026</span>

![[c_rocm_e_20.svg]]  
/// caption  
Use `#!cpp hipMemcpy` to copy data from Host (CPU) to Device (GPU) and other way around.  
///

## Vector addition Example

![[c_rocm_e_21.svg]]  
/// caption  
Each `thread` is performing `#!cpp C[i] = A[i] + B[i]` independently and hence, there is no need for `CPU` loops.  
///

> [!NOTE] Computing `thread` index  
> The global `thread` index `i` is computed by `i = blockDim.x * blockIdx.x + threadIdx.x`
> 
> - `blockDim.x` is the number of threads in each `block`.
> - `blockIdx.x` is the index of current `block` in a `grid`.
> - `threadIdx.x` is the local index of the `thread` within its `block`.

### Code Outline

| Purpose                        | Specific Use                                   | HIP API / Code Pattern                                             |
| ------------------------------ | ---------------------------------------------- | ------------------------------------------------------------------ |
| Host (CPU) Memory Allocation   | Allocate `h_A`, `h_B`, `h_C` in host memory.   | `#!cpp float *host_buf = new float[N];`                            |
| Host Buffer Initialization     | Initialize `h_A` and `h_B` with input values.  | `#!cpp for (int i = 0; i < N; i++) { //set host array values }`    |
| Device (GPU) Memory Allocation | Allocate `d_A`, `d_B`, `d_C` in device memory. | `#!cpp hipMalloc(&device_buf, bytes);`                             |
| Host-to-Device Data Transfer   | Copy `h_A` → `d_A` and `h_B` → `d_B`.          | `#!cpp hipMemcpy(dst_buf, src_buf, bytes, hipMemcpyHostToDevice);` |
| `Kernel`[^2] Launch            | Launch 1 GPU thread per output element.        | `#!cpp vec_add<<<(N+tpb-1)/tpb, tpb>>>(…); //tpb: threads/block`   |
| Device-to-Host Data Transfer   | Copy values of `d_C` (GPU results) → `h_C`.    | `#!cpp hipMemcpy(dst_buf, src_buf, bytes, hipMemcpyDeviceToHost);` |
| Verify Results                 | Check values of `h_C` for correctness.         | `#!cpp for (int i = 0; i < N; i++) { //check results }`            |
| Free Device and Host Memory    | Deallocate `d_[A,B,C]` and `h_[A,B,C]`.        | `#!cpp hipFree(device_buf); delete[] host_buf;`                    |

```{.cpp .copy .annotate}
#include <hip/hip_runtime.h> // (1)!
#include <stdio.h>

__global__ void vec_add(const float* A, const float* B, float* C, int N) { // (2)!
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    if (i < N) C[i] = A[i] + B[i];
}

int main() { // (3)!
    const int N  = 1 << 20;             // 1,048,576 elements
    size_t bytes = N * sizeof(float);   // 4 MiB per vector

    float *h_A = new float[N]; // (4)!
    float *h_B = new float[N];
    float *h_C = new float[N];

    for (int i = 0; i < N; i++) { // (5)!
        h_A[i] = i * 1.0f;
        h_B[i] = i * 2.0f;
    }

    float *d_A, *d_B, *d_C; // (6)!
    hipMalloc(&d_A, bytes); // (7)!
    hipMalloc(&d_B, bytes);
    hipMalloc(&d_C, bytes);

    hipMemcpy(d_A, h_A, bytes, hipMemcpyHostToDevice); // (8)!
    hipMemcpy(d_B, h_B, bytes, hipMemcpyHostToDevice);

    int thr_per_blk = 256;
    int blk_in_grid = (N + thr_per_blk - 1) / thr_per_blk;

    vec_add<<<blk_in_grid, thr_per_blk>>>(d_A, d_B, d_C, N); // (9)!

    hipMemcpy(h_C, d_C, bytes, hipMemcpyDeviceToHost); // (10)!

    int errs = 0; // (11)!
    for (int i = 0; i < N; i++)
        if (h_C[i] != i * 3.0f) errs++;
    printf("Vector Add: N=%d, Errors=%d - %s\n",
           N, errs, errs ? "FAIL":"PASS");

    for (int i = 0; i < 5; i++) {
        printf("  C[%d] = %.1f\n", i, h_C[i]);
    }

    hipFree(d_A); hipFree(d_B); hipFree(d_C); // (12)!
    delete[] h_A; delete[] h_B; delete[] h_C;

    return errs ? 1 : 0; // (13)!
}
```

1. Makes HIP available to the program - including `memory management`, `data transfers`, `kernel launches`,[^2] and `GPU kernel`[^2] constructs.
2. A `kernel`[^2] (runs on `GPU`) which adds 2 elements and stores the result into 3rd array.
3. Host-side entry point that coordinates `memory allocation`, `data transfers`, `kernel launch`,[^2] `verification`, and `cleanup`.
4. Host arrays memory allocation. The `h_` prefix is to indicate these arrays belong to the host.
5. Initializing host arrays.
6. The `d_` prefix is to indicate these arrays belong to the host.
7. Allocating memory on the `GPU`.
8. Transfers data from host to device.
9. Triple chevron syntax to launch the `kernel`.[^2]
10. Transfers data from device to host.
11. Verifying results
12. Deallocating memory
13. Exiting

> [!NOTE] `Kernel launches`[^2] are async with respect to the host.

```{.cpp .copy .annotate}
kernel_name <<< blocks_in_grid,
				threads_per_block,
				[optional] bytes_of_dynamic_shared_memory, // (1)!
				[optional] stream_id >>> // (2)!
	(ARG1, ARG2, ... );
```

1. `0` by default
2. `0` by default

> [!NOTE] `#!cpp hipGetLastError()`  
> Used here to detect immediate `kernel launch`[^2] errors.

> [!NOTE] `#!cpp hipDeviceSynchronize()`  
> Used here to detect errors that occurred during asynchronous `kernel execution`.[^2]

```{.cpp .copy .annotate}
hipEvent_t start, stop;
hipEventCreate(&start);
hipEventCreate(&stop);

// Record start in the kernel's stream
hipEventRecord(start, 0);

vec_add <<<grid, block>>>(d_A, d_B, d_C, N);

// Record stop in the same stream
hipEventRecord(stop, 0);
hipEventSynchronize(stop);

float ms;
hipEventElapsedTime(&ms, start, stop);
printf("vec_add: %.3f ms\n", ms);

hipEventDestroy(start); hipEventDestroy(stop);
```

1. Create two events
2. Record start in the `kernel`[^2]'s stream
3. Launch `kernel`[^2] (or `HIP`[^1] API call) in that stream
4. Record stop in the same stream
5. Wait for the stop event
6. Read elapsed $ms$.
7. Destroy both events

> [!NOTE] What is `HIP Stream`  
> An ordered queue of `GPU` work, such as `kernel launches`[^2] and `memory copies`.  
> Operations in one stream are processed in submission order, while different streams may overlap.  
> Here, `O` means the default stream; the events mark points in that queue.

|                  | hipify-perl                                                                                         | hipify-clang                                                                                           |
| ---------------- | --------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------ |
| **Approach**     | Regex-based translation                                                                             | Clang-based translation                                                                                |
| **Summary**      | Easy to run; no `CUDA` installation required                                                        | Better for complex `C++`; requires `CUDA` installation                                                 |
| **How it works** | Uses regular-expression rules to replace recognized CUDA APIs and syntax with HIP equivalents       | Uses `Clang` to parse `CUDA` as `C++` before translating it to `HIP`                                   |
| **Handles**      | Most `CUDA` APIs, types, keywords, include directives, and `kernel-launch`[^2] syntax                     | Supported `CUDA` APIs and syntax in code that uses templates, namespaces, and other complex constructs |
| **Use when**     | The code uses common `CUDA` features that translate cleanly to `HIP` and minimal setup is preferred | The code uses complex `C++` and a `CUDA` installation is available                                     |

```powershell
hipify-perl -examine vec_add.cu           # Report translation statistics without writing output
hipify-perl vec_add.cu -o vec_add.hip     # Translate the CUDA source to HIP
hipcc -o vec_add vec_add.hip && ./vec_add # Build and run the HIP program
```

## References

[^1]: Read more about [[ROCm_01|HIP]].
[^2]: Read more about [[ROCm_02|Kernels]].