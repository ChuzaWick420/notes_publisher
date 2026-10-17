---
Provider: AMD
Platform: AMD AI Developer Program, AMD AI Academy
---

# 5. Profiling and Performance Optimizations

<span style="color: gray;">Dated: 17-10-2026</span>

x-axis = Arithematic intensity - how much FLOPS were performed for each byte moved between HBM and GPU.  
y-axis = Performance, Flops per second

slope = available memory bandwidth, Line itself is the ceiling.

## Roofline Model

![[c_rocm_e_20.svg]]

> [!NOTE] Description of Axes
> - $x^+$ is `arithmetic intensity` is the `floating-point` work performed by a `kernel` divided by bytes transferred between `HBM` and the `GPU`.
> - $y^+$ is `performance` — number of `floating-point operations` performed per second.

> [!EXAMPLE] `FP32` `SAXPY` (Single precision ax + y - $y = a \times x + y$) operation  
> Total Operations = 2
> 
> 1. Multiply: $a \times x$
> 2. Add: $+ y$
> 
> Theoretical `HBM` traffic: `read x` + `read y` + `write y` = 12 bytes  
> Theoretical `arithmetic intensity`: $\frac{2 \text{ FLOPs}}{12 \text{ bytes}} = 0.17 \frac{\text{FLOP}}{\text{byte}}$
> 
> As it falls under memory bandwidth limited region, it is memory bound.

### 3 Common `GPU` Bottlenecks

| **CATEGORY**           | **DESCRIPTION / CEILING**                                                              | **ROOFLINE VIEW**                                                                    | **TYPICAL OPTIMIZATIONS**                                                                                        |     |
| ---------------------- | -------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------------------------------- | --- |
| **MEMORY-BOUND**       | HBM bandwidth sets the performance ceiling.                                            | Left of the ridge; memory bandwidth sets the ceiling.                                | Move fewer bytes, coalesce accesses, and reuse data.                                                             |     |
| **COMPUTE-BOUND**      | Compute throughput sets the performance ceiling.                                       | Right of the ridge; compute throughput sets the ceiling.                             | Use optimized libraries or instructions, reduce unnecessary work, or use lower precision where accuracy permits. |     |
| **OVERHEAD-DOMINATED** | Kernel launches, synchronization, or too little work per launch dominate elapsed time. | May sit far below the roofline; roofline position alone does not identify the cause. | Batch or fuse small operations, reduce launches and synchronization, and increase useful work per launch.        |     |

> [!NOTE] A real application can contain a mixture of these.

## Profiling

- Starting with `kernel` timing to find where time is spent.

```bash
# First pass: identify important kernels
$ rocprofv3 --kernel-trace --stats --output-format csv -- ./app

# Second pass: collect a focused counter set
$ rocprofv3 --pmc <selected counters> --output-format csv -- ./app
```

### Kernel Timing

Start here: which `kernel` consumes meaningful total time?

- `AverageNs` — Average time per launch
- Calls — Number of launches
- `TotalDurationNs` / Percentage — Contribution to total kernel time

### Compute Evidence

Clue: high arithmetic activity with modest memory pressure

- `Wavefront` activity — How much parallel work was dispatched.
- Vector / matrix instruction activity — How much arithmetic work was executed.
- Active-lane utilization — How fully the `wavefront` lanes participated.

### Memory Evidence

Clue: high traffic or stalls relative to compute activity

- Bytes read / written — How much memory traffic was generated.
- Memory-unit activity — How heavily the memory path was used.
- Memory stalls / wait cycles — How often data access delayed progress.

## How to Improve Performance

### 1. Profile

```powershell
rocprofv3 --kernel-trace --stats -- ./app
```

### 2. Is `GPU` Work Fragmented?

many short `kernels` or gaps between launches?

#### Yes - overhead Dominated

Tell: Many short `kernels` or large gaps; little useful work per `launch`.

Optimize: Batch or fuse work, reduce `launches` and `synchronization`, and increase useful work per launch.

#### No

##### 3. What Sets the Performance Ceiling?

###### Memory-bound

Tell: Left of the ridge; HBM bandwidth sets the ceiling.  
Optimize: Move fewer bytes, coalesce accesses, and reuse data.

###### Compute-bound

Tell: Right of the ridge; compute throughput sets the ceiling.  
Optimize: Use optimized libraries or instructions, reduce unnecessary work, and use lower precision where accuracy permits.

## Matrix Transpose

![[c_rocm_e_21.svg]]

> [!NOTE] The challenge  
> Adjacent `threads` read contiguous elements from an input row but write strided elements to an output column. This access mismatch is the main optimization challenge

![[c_rocm_e_22.svg]]  
/// caption  
Elements in the same row are contiguous in memory, while elements in the same column are one row stride apart.  
///

### Mapping 2D `HIP` Grid onto the `Matrix`

![[c_rocm_i_5.png]]

> [!NOTE]
> - Grid: $2 \times 2$ blocks
> - Block: $4 \times 4$ threads
> - Thread Space: $8 \times 8$
> - Total threads: $4 \times 16 = 64$
> - Matrix: $7 \times 7 = 49$ elements
> - Out of Bounds: $15$ threads

> [!NOTE] Thread Launch configuration
> 
> ```cpp
> dim3 thr_per_blk(4, 4);
> dim3 blk_in_grid(
> 	(width  + thr_per_blk.x - 1) / thr_per_blk.x),
> 	(height + thr_per_blk.y - 1) / thr_per_blk.y)
> );
> ```

> [!NOTE] Global Thread Coordinates
> 
> ```cpp
> int col
> int row
> 
> = blockIdx.x* blockDim.x + threadIdx.x;
> = blockIdx.y * blockDim.y + threadIdx.y;
> ```

> [!NOTE] Bounds Check & Linear (1D) Index
> 
> ```cpp
> if (row < height && col < width) {
> 	int index = row * width + col;
> 	// Process A[index]
> }
> ```

> [!EXAMPLE] A Specific Thread Mapping Example  
> This thread maps to logical element `#!cpp A[5][6]`, stored at linear location `#!cpp A[41]`.
> ```cpp
> blockIdx = (1, 1); 
> threadIdx = (2, 1);
> 
> col   = 1 * 4 + 2 = 6;
> row   = 1 * 4 + 1 = 5;
> index = 5 * 7 + 6 = 41;
> ```

### Baseline `kernel`

> [!NOTE] Each `thread` reads one input element and writes it directly to the transposed output-one element per thread, with no shared memory (`LDS`).

```cpp
__global__ void transpose_baseline (const float* in, float* out, int width, int height) {
	int col = blockIdx.x * blockDim.x + threadIdx.x;
	int row = blockIdx.y * blockDim.y + threadIdx. y;
	
	if (col < width && row < height) {
		out [col * height + row] // (1)!
		= 
		in[row * width + col]; // (2)!
		
		// 2. Consecutive col values access output elements height apart
	}
}
```

1. `#!cpp out[col * height + row]` advances by height elements - strided outputs
2. `#!cpp in[row * width + 0]` advances by one element - contiguous input reads

> [!NOTE] What the code does  
> Each `thread` reads one input element from global memory and writes it directly to its transposed output location.

> [!WARNING] Optimization Goal  
> Keep one global load and one global store per element, but reorganize the global accesses so neighboring `threads` use neighboring addresses.

### Memory Coalescing

![[c_rocm_e_23.svg]]  
/// caption  
Coalesced - consecutive lanes -> consecutive addresses -> fewer, wider transactions  
///

> [!NOTE] 
> - Thread 0 → `#!cpp addr[k]`
> - Thread 1 → `#!cpp addr[k + 1]`
> - Thread 2 → `#!cpp addr[k + 2]`
> - Neighboring lanes access neighboring addresses
> - Requests combine into wide, aligned transactions
> - High transaction efficiency

---

![[c_rocm_e_24.svg]]  
/// caption  
Strided - consecutive lanes -> strided addresses -> many transactions  
///

> [!NOTE]
> - Thread 0 → `#!cpp addr[k]`
> - Thread 1 → `#!cpp addr[k + stride]`
> - Thread 2 → `#!cpp addr[k + 2 * stride]`
> - Neighboring lanes access widely separated addresses
> - Requests span many memory regions
> - Lower transaction efficiency and effective bandwidth

### Shared Memory (`LDS`) Staging

![[c_rocm_e_25.svg]]  
/// caption  
`Threads` cooperatively load the input tile row-wise into `LDS`, then synchronize before reading it back. Then `threads` read the same `LDS` tile with swapped indices and write the transposed tile row-wise to global memory.  
///

```cpp
__shared__ float tile[TILE][TILE];
	int in_col = blockIdx.x * TILE + threadIdx.x;
	int in_row = blockIdx.y * TILE + threadIdx.y;
	
	if (in_col < width && in_row < height)
		tile[threadIdx.y][threadIdx.x] = in[in_row * width + in_col]; // coalesced read
		
	__syncthreads();
```

```cpp
int out_col = blockIdx.y * TILE + threadIdx.x;
int out_row = blockIdx.x * TILE + threadIdx.y;

if (out_col < height && out_row < width)
	out[out_row * height + out_col] = tile[threadIdx.x][threadIdx.y]; // coalesced write
```

### Optimized `kernel`

```cpp
#define TILE 16

__global__ void transpose_optimized(const float* in, float* out, int width, int height) {
    __shared__ float tile[TILE][TILE + 1]; // +1 padding reduces LDS bank conflicts

    // Input coordinates in the original height x width matrix
    int in_col = blockIdx.x * TILE + threadIdx.x;
    int in_row = blockIdx.y * TILE + threadIdx.y;

    // Load the input tile row-wise into LDS
    if (in_col < width && in_row < height) {
        tile[threadIdx.y][threadIdx.x] = in[in_row * width + in_col];
    }

    __syncthreads(); // The entire workgroup must finish loading the tile

    // Swap the block coordinates for the transposed output
    int out_col = blockIdx.y * TILE + threadIdx.x;
    int out_row = blockIdx.x * TILE + threadIdx.y;

    // Output has width rows x height columns
    if (out_col < height && out_row < width) {
        out[out_row * height + out_col] = tile[threadIdx.x][threadIdx.y];
    }
}
```

> [!NOTE]- Changes compared to baseline `kernerl`  
> - +1 padding: reduces LDS bank conflicts during transposed reads.
> - Coalesced load: Neighboring threads read neighboring global-memory addresses into an LDS row.
> - Synchronize: Wait until the tile is fully loaded before any thread reads values written by another thread.
> - Swapped LDS read + row-wise store: The baseline's strided write becomes a coalesced global store.

## `SAXPY` - Single Precision Ax plus Y

### Baseline `Kernel`

```cpp
__global__ void saxpy(float a, const float* x, float* y, int N) {
	int i = blockDim.x * blockIdx.x + threadIdx.x; // 1 element / thread
	if (i < N) y[i] = a * x[i] + y[i];             // 2 reads, 1 write
}
```

```cpp
// Kernel launch configuration
int thr_per_blk = 256;
int blk_in_grid = (N + thr_per_block - 1) / thr_per_blk;

saxpy<<blk_in_grid, thr_per_blk>>(a, d_x, d_y, N);
```

![[c_rocm_e_26.svg]]  
/// caption  
Memory bound performance ceiling for `SAXPY`: $\left(5.3 \frac{\text{TB}}{s}\right) \times 0.17 \frac{\text{FLOPs}}{B} \approx 0.88 \frac{\text{FLOPs}}{s}$  

- Measure average time (`ns`) to run `SAXPY` size `N` .

```
rocprofv3 --kernel-trace --stats --output-format csv -- ./saxpy
```

- Calculate effective bandwidth (`GB/s`)  

$$\text{Effective Bandwidth} = \frac{12N}{t_{\text{avg}, \text{ ns}}}$$

- Calculate measured performance ($P_{\text{measured}}$)  

$$P_{\text{measured}} = B_{\text{effective}} \times I_{\text{SAXPY}}$$

///

### Sweep the Block Size

```cpp
int thr_per_blk = ...; // 64, 128, 256, 512
int blk_in_grid = (N + thr_per_blk - 1) / thr_per_blk;

saxpy<<<blk_in_grid, thr_per_blk>>>(a, d_x, d_y, N);
```

| Threads / block | Average Kernel time | Effective bandwidth | Bandwidth utilization \% |
| --------------- | ------------------- | ------------------- | ------------------------ |
| 64              | -                   | -                   | -                        |
| 128             | -                   | -                   | -                        |
| 256             | -                   | -                   | -                        |
| 512             | -                   | -                   | -                        |

> [!NOTE] All block sizes remain at $I = 0.17$ FLOP/byte. Sweep the block size to find the point where bandwidth plateaus; beyond that, larger blocks provide little benefit.

> [!NOTE] Experiment Procedure
> 1. Use the same N, inputs, warm-up count, and number of timed launches.
> 2. Run `64`, `128`, `256`, and `512` threads per block as separate profiling runs.
> 3. Record average time using `rocprofv3 --kernel-trace --stats --output-format csv -- ./saxpy <threads_per_block>`
> 4. Calculate and compare  
> 
> $$B_{\text{effective}} = \frac{12N}{t_{\text{avg, ns}}} \quad BW_{\text{utilization}} = \frac{B_{\text{effective}}}{B_{\text{ceiling}}}$$

## Mixed Precision `GEMM` - Throughput Vs Accuracy

> [!NOTE]
> - `FP16` / `BF16` operands can increase `GEMM` throughput
> - `FP32` accumulation reduces summation error.

| Format | Bits | Exponent | Fractional Bits | Decimal Digits |
| ------ | ---: | -------: | --------------: | -------------: |
| FP32   |   32 |        8 |              23 |             ~7 |
| FP16   |   16 |        5 |              10 |           ~3–4 |
| BF16   |   16 |        8 |               7 |           ~2–3 |

> [!NOTE] Why it is faster  
> 16-bit operands use half the storage of `FP32`, reducing operand traffic. 

> [!NOTE] The Tradeoff  
> `FP16` / `BF16` round the input values. `FP32` accumulation reduces error as the products are summed, but cannot recover precision already lost in the inputs.

> [!NOTE] The Experiment  
> Run the same `M = N = K = 2048` `GEMM` in `FP32`, `FP16`, and `BF16`. Compare runtime, TFLOP/s, and error relative to the `FP32` result.

```python
device = torch.device("cuda")   # ROCm uses PyTorch's CUDA API
M = N = K = 2048

# One source problem for all three tests
A32 = torch.rand(M, K, device=device)
B32 = torch.rand(K, N, device=device)
C_ref = torch.mm(A32, B32)

for dtype in [torch.float32, torch.float16, torch.bfloat16]:

    A = A32.to(dtype)
    B = B32.to(dtype)

    warm_up(torch.mm, A, B)
    ms = time_gpu(torch.mm, A, B, repeats=50)   # Average ms/GEMM

    C = torch.mm(A, B)   # Untimed result for comparison
    tflops = 2 * M * N * K / (ms * 1e9)
    difference = relative_difference(C.float(), C_ref)

    report(dtype, ms, tflops, difference)
```

| Operand `dtype` | Avg. time (ms) | TFLOP/s | Rel. difference vs. FP32 |
| --------------- | -------------- | ------- | ------------------------ |
| `FP32`          | -              | -       | reference                |
| `FP16`          | -              | -       | -                        |
| `BF16`          | -              | -       | -                        |

> [!NOTE] Choose the fastest precision that stays within the workload's numerical tolerance.

> [!NOTE]
> - `#!cpp time_gpu()` returns the average elapsed milliseconds per `GEMM` using `GPU` events and synchronization. 
> - `#!cpp relative_difference()` compares the result with the `FP32` reference.