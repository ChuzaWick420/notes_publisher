---
Provider: AMD
Platform: AMD AI Developer Program, AMD AI Academy
---

# 3. Libraries

<span style="color: gray;">Dated: 15-10-2026</span>

![[c_rocm_e_6.svg]]  
/// caption  
`ROCm` libraries sit between the `HIP`[^1] runtime and the application.  
///

| Library                 | What It Does                                           | Where It's Used                                        |
| ----------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| **rocBLAS / hipBLASLt** | Provides dense linear algebra operations, such as GEMM | Accounts for much of the computation in modern AI      |
| **MIOpen**              | Provides deep learning primitives, such as convolution | Convolution layer in CNNs                              |
| **rocFFT**              | Provides Fast Fourier Transforms in 1D, 2D, and 3D     | Signal processing, spectral methods, physics           |
| **rocSOLVER**           | Provides matrix factorizations and solvers             | Scientific computing, PCA, regression                  |
| **rocRAND**             | Generates pseudo-random and quasi-random numbers       | Simulation, sampling, Monte Carlo                      |
| **rocSPARSE**           | Provides sparse matrix and vector operations           | Scientific solvers, graph workloads, sparse data needs |
| **rocPRIM / hipCUB**    | Provides parallel primitives, such as scan, sort       | Custom kernel building blocks                          |

## rocBLAS / hipBLASLt — Dense Linear Algebra[^2]

### What it Does

- Vector - Vector — `AXPY`, `DOT`, `SCAL`, `NRM2`
- Matrix - Vector — `GEMV`, `TRSV`
- Matrix - Matrix — `GEMM`, `TRSM`

> [!NOTE] General Matrix Multiplication  
$\text{GEMM}: D = \alpha \times A \times B + \beta \times C$

### Why it is Fast

- Calls `MFMA`[^3] matrix engine
- Tile sizes are selected per `CDNA` generation to maximize data reuse in `LDS` and saturate the `MFMA`[^3] engines
- Software pipeline depth is tuned to hide memory latency behind compute and keep the `MFMA`[^3] units busy

## MIOpen — Deep Learning Primitives

### Operations

- Convolution — forward + backward, 2D / 3D, multi-algo  
- Batch norm — training and inference modes  
- Pooling — max / average, with optional indices  
- Activations — `ReLU`, `GELU` (via graph API)  
- `RNN` / `LSTM` / `GRU` — fused recurrent cells  
- `Softmax` — fast, accurate, and `log-softmax`

### Features

- Multi-algorithm dispatch — Example: `Winograd`, `GEMM`, direct, implicit-`GEMM` - picked per shape
- Two-tier autotune — `FindDb` chooses algorithm, `PerfDb` tunes its parameters
- Multi-precision — `fp32`, `fp16`, `bf16`, `int8`
- Operator fusion — conv + bias + activation in a single `kernel`[^4]

!!! TIP Why fuse matters
	> === "Without Fuse"
	> 	```mermaid
	> 	flowchart LR
	>		id1[conv]
	> 		id2[HBM]
	> 		id3[bn]
	> 		id4[HBM]
	> 		id5[relu]
	> 		id1 --> id2 --> id3 --> id4 --> id5
	> 	```
	> 
	> === "With Fuse"
	> 	```mermaid
	> 	---
	> 	title: reduces off chip memory access, avoids kernel launch overhead
	> 	---
	> 	flowchart LR
	> 		id1[conv + bn + relu]
	> 		id1 --> HBM
	> 	```

### `MIOpen` Autotune

> [!QUESTION] `FindDb` — Which Solution should be used?  
> Remembers the best MIOpen implementation for a convolution problem.

> [!QUESTION] `PerfDb` — How should it be tuned?  
> Remembers low-level `kernel`[^4] tuning choices, such as tile size or block size.  

> [!QUESTION] `Kernel cache` — Is the GPU code already compiled?  
> Reuses compiled GPU `kernels`[^4] to avoid recompilation.

![[c_rocm_e_7.svg]]

## rocFFT — Fast Fourier Transforms

$$\text{Time Domain} \longleftrightarrow \text{Frequency Domain}$$

### What it Supports

- 1D / 2D / 3D — arbitrary lengths
- Real & Complex FFTs — `R2C` / `C2R` / `C2C`
- Batched FFTs — process $N$ signals at once
- Precisions — `FP16` / `FP32` / `FP64`

### Where You Use it

- Signal processing — audio, radar, telecom
- Physics simulations — fluid dynamics, electromagnetics
- Medical imagining — MRI reconstruction

## rocSOLVER - Linear Algebra Decompositions

| Decomposition  | Equation                       | Reveals                                                                         | Solves                                                         |
| -------------- | ------------------------------ | ------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| **LU**         | $A = L \cdot U$                | Lower and upper-triangular factors.                                             | General linear systems $Ax = b$.                               |
| **Cholesky**   | $A = L \cdot L^T$              | For SPD matrices: only one triangle needs storing. Half the work of `LU`.       | - Symmetric pos-def systems<br>- normal eqns<br>-GPs           |
| **QR**         | $A = Q \cdot R$                | Q has orthonormal columns ($Q^T Q = I$). Stable solving without inverses.       | - Least squares <br>- regression<br>- over-determined systems  |
| **SVD**        | $A = U \cdot \Sigma \cdot V^T$ | Singular values in $\Sigma$ rank importance. Drop the small ones ~ compression. | - PCA<br>- low-rank approx<br>- recommender<br>- denoising     |
| **Eigenvalue** | $A \cdot v = \lambda \cdot v$  | Special directions $v$ that $A$ only stretches. $\lambda$ = stretch factor.     | - Spectral analysis<br>- PageRank<br>- stability<br>- dynamics |

## rocRAND — Pseudo vs. Quasi-random Generators

=== "PRNG - Pseudo-random"

	> [!INFO] Goal  
	> Look random and statistically independent enough for simulation.

	> [!NOTE]  
	> Deterministic algorithm + seed -> reproducible sequence that passes statistical randomness tests.

	![[c_rocm_e_8.svg]]  
	/// caption  
	clustered — has gaps  
	///
	
	- `XORWOW` — xorshift; fast, simple bit ops
	- `MT19937` — Mersenne Twister
	- `MTGP32` — MT variant tuned for GPUs
	- `Philox` — counter-based, parallel-friendly
	- `MRG32K3A` / `MRG31K3P` — combined multiple recursive
	- `LFSR113` — linear-feedback shift register
	- `ThreeFry` — counter-based, Threefish cipher
	
	> [!INFO] Best for
	> - Simulation
	> - Sampling
	> - Randomized algorithms
	> - Stochastic ML kernels

=== "QRNG — Quasi-random"

	> [!INFO] Goal  
	> Fill the space uniformly (low discrepancy).

	> [!NOTE]  
	> Points are constructed to reduce gaps and clumping. No seed like PRNG - indexed by dimension and offset.

	![[c_rocm_e_9.svg]]  
	/// caption  
	uniform — no clumping  
	///

	- `Sobo132` — 32-bit Sobol low-discrepancy
	- `Sobo164` — 64-bit; higher-resolution output
	- Scrambled `Sobo132` — scrambled for randomization; with low discrepancy
	- Scrambled `Sobo164` — scrambled 64-bit variant

	> [!INFO] Best for
	> - Quasi-Monte Carlo
	> - Numerical Integration
	> - Ray Tracing
	> - Finance
	> - Option Pricing

---

## rocSPARSE - Sparse Matrix Operations

> [!INFO] Core Operations
> - `SpMV`
> - `SpMM`
> - `SpGEMM`
> - `SDDMM`
> - `Sparse solves`
> - `Format conversion`

| Format  | Description                                                           |
| ------- | --------------------------------------------------------------------- |
| **CSR** | `Compressed Sparse Row` — most common — fast `SpMV`                   |
| **CSC** | `Compressed Sparse Column` — column-oriented operations               |
| **COO** | `Coordinate list` — easy to assemble, sort, and convert               |
| **ELL** | Fixed-width — best when row sizes are uniform                         |
| **BSR** | `Block Sparse Row` — for dense sub-blocks (e.g. FEM)                  |
| **HYB** | `Hybrid ELL` + `COO` — reg. rows in `ELL`, `irreg`. overflow in `COO` |

> [!EXAMPLE] Memory Saved Example  
> $10,000 \times 10,000$ `matrix`, $0.1\%$ density (typical `GNN` adjacency)
> - Dense (`fp32`): <span style="color: red;">400 MB</span>
> - `CSR` sparse: $\approx$ <span style="color: cyan;">840 MB</span>  
> $\approx475\times$ smaller and only non zeroes are touched in compute.

## rocPRIM / hipCUB — Parallel Primitives

![[c_rocm_i_1.svg]]  
/// caption  
Generated with Claude Sonnet 5.5. Proofread by self.  
///  

![[c_rocm_i_2.svg]]  
/// caption  
Generated with Claude Sonnet 5.5. Proofread by self.  
///  

![[c_rocm_i_3.svg]]  
/// caption  
Generated with Claude Sonnet 5.5. Proofread by self.  
///  

![[c_rocm_i_4.svg]]  
/// caption  
Generated with Claude Sonnet 5.5. Proofread by self.  
///

## `Triton` Kernel Language and Compiler on `AMD`

> [!NOTE] Beyond `ROCm` Libraries
> - `Triton` (`Python` based Domain Specific Language) for custom `kernels`
> - `HIP`[^1] or full control

| Feature / Aspect            | ROCm Libraries                                                       | Triton                                                       | Raw HIP                                                         |
| --------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **Technology / Stack**      | Pre-built library functions (`rocBLAS`, `MIOpen`, `hipBLASLt`, etc.) | Python DSL (`@triton.jit`) for custom kernels with less code | HIP C++ kernels compiling via `amdclang/LLVM` to AMD GPU binary |
| **Usage Example**           | `#!python torch.matmul(a, b)`                                        | Fused, custom, portable kernels                              | Low-level C++ code                                              |
| **Advantages**              | Easiest path for standard operations                                 | Flexible path for custom kernels                             | Maximum low-level control                                       |
| **Trade-offs / Challenges** | Limited flexibility for custom kernel fusion                         | Still requires GPU-kernel thinking                           | Most code and tuning effort required                            |

> [!TIP] Why use `Triton`
> - `Python` Kernel `DSL` — Write block-level logic; Triton compiles it for the GPU
> - Portable across vendors — Same source can target AMD and NVIDIA backends; tuning may differ.
> - Auto tuning built in — `@triton.autotune` benchmarks supplied configs and select best one for a shape.
> - Used by `#!python torch.compile` — `#!python torch.compile` uses `TorchInductor`; on AMD GPUs `Triton` is a key GPU codegen path.

## PyTorch On ROCm — Familiar Workflows and Ecosystem

![[c_rocm_e_10.svg]]  
/// caption  
The full stack  
///

### Common Ai Workflows

#### Train and Fine Tune

- Single- & multi-GPU training on Instinct  
- `HF` Transformers + `PEFT`  
- `LoRA` / `QLoRA` for `LLM` fine-tuning  
- `FSDP` / DeepSpeed `ZeRO` / Lightning

#### Serve

- `vLLM`, `SGLang`, `TGI` - OpenAI-compatible APIs  
- `KV-cache` management, continuous batching  
- `FP8` `GEMM` paths on `CDNA 3` and newer  
- Large throughput gains vs naive serving

#### Research

- Rapid prototyping with standard `PyTorch` workflows
- Lightning, Hydra, `W&B`, Diffusers, `HF`

## How `#!python torch.compile()` Optimizes PyTorch

### Without `#!python torch.compile()` — Eager Mode

![[c_rocm_e_11.svg]]  
/// caption  
Separate ops often mean separate GPU launches and temporary memory writes.  
///

> [!TIP] Eager: More launches and temporary data

### With `#!python torch.compile()` $\textemdash$ Graph Capture + Fused Eligible Ops

![[c_rocm_e_12.svg]]  
/// caption  
Captures graph regions, fuses eligible ops; fewer GPU launches and temporary memory writes.  
///

> [!TIP] Compiled: Fewer launches and temporary data

```python
model = torch.compile(model) # default backend = TorchInductor; on AMD it emits Trition kernels and calls ROCm libraries.
```

## RCCL — Multi-GPU and Multi-node Communication

=== "All Reduce"
	> ![[c_rocm_e_13.svg]]  

	> | **Before**              | **After**            |
	> | ----------------------- | -------------------- |
	> | Every GPU has 1 element | Every GPU has $\sum$ |

	> [!NOTE]  
	> - Each GPU contributes a same-size array
	> - All receive the reduced array
	
	> [!TIP] Used in  
	> Data-parallel training (gradient sync)

=== "All Gather"
	> ![[c_rocm_e_14.svg]]  

	> | **Before**              | **After**                    |
	> | ----------------------- | ---------------------------- |
	> | Every GPU has 1 element | every GPU has the full array |

	> [!NOTE]
	> - Each GPU contributes 1 chunk
	> - All receive the concatenated array
	
	> [!TIP] `FSDP` / `ZeRO-3` (gather sharded parameters)

=== "Reduce Scatter"
	> ![[c_rocm_e_15.svg]]  

	> | **Before**          | **After**                  |
	> | ------------------- | -------------------------- |
	> | Each has full array | Each holds 1 reduced chunk |

	> [!NOTE]
	> - Reduce across GPUs
	> - Each receives 1 reduced chunk
	
	> [!TIP] `FSDP` / `ZeRO-3` (reduce and shard gradients)

=== "Broadcast"
	> ![[c_rocm_e_16.svg]]  

	> | **Before**         | **After**         |
	> | ------------------ | ----------------- |
	> | Only 1 GPU has `a` | All GPUs have `a` |
	
	> [!NOTE] 
	> - One GPU provides an array
	> - All receive the same array
	
	> [!TIP] Initial parameter / state sync

=== "All to All"
	> ![[c_rocm_e_17.svg]]  

	> | **Before**        | **After**              |
	> | ----------------- | ---------------------- |
	> | Each has 2 chunks | Grouped by destination |

	> [!NOTE] Each GPU contributes 1 chunk per destination and receives 1 from each destination

	> [!TIP] `MoE` token routing (tokens → expert GPU)

---

## PyTorch And vLLM for Inference on ROCm

> [!INFO]
> - `PyTorch` provides the model framework
> - `vLLM` uses it within a specialized `LLM` inference and serving engine.

### Direct PyTorch Inference

- General-purpose — `LLMs` and other model types
- Flexible execution — direct control over model and pipeline
- Custom workflows — preprocessing, logic, and outputs
- Simple deployment — scripts, applications, or services

### vLLM Inference & Serving

- Paged Attention — manages KV cache in page-like blocks
- Continuous batching — dynamically batches active requests
- Quantization — lower precision reduces memory use
- integrates with compatible clients — OpenAI-compatible API

Run `vLLM` on `ROCm` - official image, familiar CLI and API

```powershell
docker run --rm \
	--group-add=video \
	--cap-add=SYS_PTRACE \
	--security-opt seccomp=unconfined\
	--device=/dev/kfd \
	--device=/dev/dri \
	--ipc=host \
	-p 8000:8000
	-v /path/to/model:/model \
	vllm/vllm-openai-rocm: latest \ # Pull the official ROCm vLLM image
	--model /model
```

## References

[^1]: Read more about [[ROCm_01|HIP]].
[^2]: Read about [[mth501_01|Linear Algebra]].
[^3]: Read more about [[ROCm_02|MFMA — Matrix Fused Multiply Add]].
[^4]: Read more about [[ROCm_02|Kernel]].
