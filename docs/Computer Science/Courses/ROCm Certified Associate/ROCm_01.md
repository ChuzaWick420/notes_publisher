---
Provider: AMD
Platform: AMD AI Developer Program, AMD AI Academy
---

# Introduction

<span style="color: gray;">Dated: 01-10-2026</span>

![[c_rocm_e_1.svg]]

ROCm is open source and provides a migration path for CUDA through HIP.

> [!NOTE] ==**Heterogeneous-computing Interface for Portability (HIP)**== is a C++ runtime API and kernel programming language created by AMD that lets developers build high-performance, single-source applications for both AMD and NVIDIA graphics cards.[^1]

- HIP provides a CUDA like c++ programming model.  
- Hipify helps migrate existing `CUDA` source code to `HIP`.
- Used across hyperscale AI, public cloud and HPC.
	- Azure MI300X
	- OCI MI355X
	- EI Capitan MI300A
	- Frontier MI250X super computers

## Core `ROCm` Components Grouped by roles[^2]

![[c_rocm_e_2.svg]]

![](https://rocm.docs.amd.com/en/docs-7.2.4/_images/rocm-software-stack-7_2_1.png)  

## Compatibility Matrix[^3]

| **Family / Product Line** | **Product**                        | **Architecture** | **LLVM Target** |     |
| ------------------------- | ---------------------------------- | ---------------- | --------------- | --- |
| **Instinct**              | MI355X, MI350X, MI350P             | CDNA 4           | gfx950          |     |
| **Instinct**              | MI325X, MI300X, MI300A             | CDNA 3           | gfx942          |     |
| **Instinct**              | MI250X, MI250, MI210               | CDNA 2           | gfx90a          |     |
| **Instinct**              | MI100                              | CDNA 1           | gfx908          |     |
| **Radeon**                | RX 9070/9060, AI PRO R9700         | RDNA 4           | gfx1200/1201    |     |
| **Radeon**                | RX 7900/7800/7700, PRO W7900/W7800 | RDNA 3           | gfx1100/1101    |     |

`HIP` maintain a single source code base that can be compiled for `AMD` or `NVIDIA` GPUs.

![[c_rocm_e_3.svg]]

## `HIP` Vs `CUDA` - Side by Side

=== "`HIP` (AMD)"  
	```{.cpp .annotate .copy hl_lines="3-6"}  
	#include <hip/hip runtime.h>
	
	__global__ void add(float* a, float* b, float* c) { // (1)!
		int i = blockIdx.x * blockDim.x + threadIdx.x;
		if (i < N) c[i] = a[i] + b[i];
	}
	
	int main () {
		float *a, *b, *c;
		
		hipMalloc(&a, N * sizeof(float)) // (2)!
		hipMalloc(&b, N * sizeof(float))
		hipMalloc(&c, N * sizeof(float))
		
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
	#include <hip/hip runtime.h>
	
	__global__ void add(float* a, float* b, float* c) { // (1)!
		int i = blockIdx.x * blockDim.x + threadIdx.x;
		if (i < N) c[i] = a[i] + b[i];
	}
	
	int main () {
		float *a, *b, *c;
		
		cudaMalloc(&a, N * sizeof(float)) // (2)!
		cudaMalloc(&b, N * sizeof(float))
		cudaMalloc(&c, N * sizeof(float))
		
		cudaMemcpy(a, h_a, N * sizeof(float), cudaMemcpyHostToDevice);
		cudaMemcpy(b, h_b, N * sizeof(float), cudaMemcpyHostToDevice);
		
		add <<<blocks, threads>>> (a, b, c);
		
		cudaMemcpy(h_c, c, N * sizeof(float), cudaMemcpyDeviceToHost);
	}
	```
	
	1. Kernel remains the same.
	2. API calls start with `cuda` prefix.

> [!TIP] `hipify-perl` renames CUDA APIs automatically.

[^1]: [What is Hip - ROCm Docs](https://rocm.docs.amd.com/projects/HIP/en/docs-6.4.2/what_is_hip.html#what-is-hip)
[^2]: [What is ROCm - ROCm docs](https://rocm.docs.amd.com/en/docs-7.2.4/what-is-rocm.html)
[^3]: [compatibility matrix](https://rocm.docs.amd.com/en/docs-7.2.4/compatibility/compatibility-matrix.html)