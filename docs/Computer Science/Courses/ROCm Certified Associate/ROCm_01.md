---
Provider: AMD
Platform: AMD AI Developer Program, AMD AI Academy
---

# 1. Introduction

<span style="color: gray;">Dated: 01-10-2026</span>

![[c_rocm_e_1.svg]]

`ROCm`[^1] is open source and provides a migration path for CUDA through `HIP`.[^2]

> [!NOTE] ==**Heterogeneous-computing Interface for Portability (HIP)**== is a C++ runtime API and kernel programming language created by AMD that lets developers build high-performance, single-source applications for both AMD and NVIDIA graphics cards.[^2]

- `HIP`[^2] provides a CUDA like c++ programming model.  
- `Hipify` helps migrate existing `CUDA` source code to `HIP`.[^2]
- Used across hyperscale AI, public cloud and HPC (High Performance Computing).
	- Azure MI300X
	- OCI MI355X
	- EI Capitan MI300A
	- Frontier MI250X super computers

## Core `ROCm` Components Grouped by roles[^1]

![[c_rocm_e_2.svg]]

![](https://rocm.docs.amd.com/en/docs-7.2.4/_images/rocm-software-stack-7_2_1.png)  

## Compatibility Matrix[^3]

| Family / Product Line | Product                                            | Architecture | LLVM Target        |
| --------------------- | -------------------------------------------------- | ------------ | ------------------ |
| **Instinct**          | `MI355X`, `MI350X`, `MI350P`                       | `CDNA 4`     | `gfx950`           |
| **Instinct**          | `MI325X`, `MI300X`, `MI300A`                       | `CDNA 3`     | `gfx942`           |
| **Instinct**          | `MI250X`, `MI250`, `MI210`                         | `CDNA 2`     | `gfx90a`           |
| **Instinct**          | `MI100`                                            | `CDNA 1`     | `gfx908`           |
| **Radeon**            | `RX 9070` / `9060`, `AI PRO R9700`                 | `RDNA 4`     | `gfx1200` / `1201` |
| **Radeon**            | `RX 7900` / `7800` / `7700`, `PRO W7900` / `W7800` | `RDNA 3`     | `gfx1100` / `1101` |

![[c_rocm_e_3.svg]]  
/// caption  
`HIP`[^2] maintain a single source code base that can be compiled for `AMD` or `NVIDIA` GPUs.  
///

## `HIP`[^2] Vs `CUDA` - Side by Side

=== "`HIP` (AMD)"  
	```{.cpp .annotate .copy hl_lines="3-6"}  
	#include <hip/hip_runtime.h>
	
	__global__ void add(float* a, float* b, float* c) { // (1)!
		int i = blockIdx.x * blockDim.x + threadIdx.x;
		if (i < N) c[i] = a[i] + b[i];
	}
	
	int main () {
		float *a, *b, *c;
		
		hipMalloc(&a, N * sizeof(float)); // (2)!
		hipMalloc(&b, N * sizeof(float));
		hipMalloc(&c, N * sizeof(float));
		
		hipMemcpy(a, h_a, N * sizeof(float), hipMemcpyHostToDevice);
		hipMemcpy(b, h_b, N * sizeof(float), hipMemcpyHostToDevice);
		
		add <<<blocks, threads>>> (a, b, c);
		
		hipMemcpy(h_c, c, N * sizeof(float), hipMemcpyDeviceToHost);
	}
	```
	
	1. Kernel remains the same.
	2. API calls start with `hip` prefix.

=== "`CUDA` (NVIDIA)"  
	```{.cpp .annotate .copy hl_lines="3-6"}  
	#include <cuda_runtime.h>
	
	__global__ void add(float* a, float* b, float* c) { // (1)!
		int i = blockIdx.x * blockDim.x + threadIdx.x;
		if (i < N) c[i] = a[i] + b[i];
	}
	
	int main () {
		float *a, *b, *c;
		
		cudaMalloc(&a, N * sizeof(float)); // (2)!
		cudaMalloc(&b, N * sizeof(float));
		cudaMalloc(&c, N * sizeof(float));
		
		cudaMemcpy(a, h_a, N * sizeof(float), cudaMemcpyHostToDevice);
		cudaMemcpy(b, h_b, N * sizeof(float), cudaMemcpyHostToDevice);
		
		add <<<blocks, threads>>> (a, b, c);
		
		cudaMemcpy(h_c, c, N * sizeof(float), cudaMemcpyDeviceToHost);
	}
	```
	
	1. Kernel remains the same.
	2. API calls start with `cuda` prefix.

> [!TIP] `hipify-perl` renames CUDA APIs automatically.

## Command-line Tools

```mermaid
flowchart LR
	Monitor --> Query --> Compile --> Profile
```

/// caption  
AMD `ROCm`[^1] development loop  
/// 

| Tool          | What It Does                                                 | When You Use It                                                 |
| ------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **amd-smi**   | GPU dashboard: temp, clocks, memory, power, utilization.     | When you want a quick health check --- is it busy? overheating? |
| **rocminfo**  | Lists GPUs and CPUs: name, CU count, ISA, wavefront, clocks. | First thing after install --- does `ROCm`[^1] see the GPU?      |
| **hipcc**     | HIP compiler – auto-detects GPU, emits native code.          | Every compile: `hipcc -O3 -o out in.hip`                        |
| **rocprofv3** | Kernel times, HW counters, occupancy metrics.                | Profiling: `rocprofv3 --stats --kernel-trace -- ./app`          |

## References

[^1]: [ROCm --- ROCm docs](https://rocm.docs.amd.com/en/docs-7.2.4/what-is-rocm.html)
[^2]: [HIP --- ROCm Docs](https://rocm.docs.amd.com/projects/HIP/en/docs-6.4.2/what_is_hip.html#what-is-hip)
[^3]: [Compatibility Matrix --- ROCm Docs](https://rocm.docs.amd.com/en/docs-7.2.4/compatibility/compatibility-matrix.html)