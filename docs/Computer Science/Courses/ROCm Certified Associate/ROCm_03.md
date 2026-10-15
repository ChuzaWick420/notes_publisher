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

| **Library**             | **What It Does**                                       | **Where It's Used**                                    |
| ----------------------- | ------------------------------------------------------ | ------------------------------------------------------ |
| **rocBLAS / hipBLASLt** | Provides dense linear algebra operations, such as GEMM | Accounts for much of the computation in modern AI      |
| **MIOpen**              | Provides deep learning primitives, such as convolution | Convolution layer in CNNs                              |
| **rocFFT**              | Provides Fast Fourier Transforms in 1D, 2D, and 3D     | Signal processing, spectral methods, physics           |
| **rocSOLVER**           | Provides matrix factorizations and solvers             | Scientific computing, PCA, regression                  |
| **rocRAND**             | Generates pseudo-random and quasi-random numbers       | Simulation, sampling, Monte Carlo                      |
| **rocSPARSE**           | Provides sparse matrix and vector operations           | Scientific solvers, graph workloads, sparse data needs |
| **rocPRIM / hipCUB**    | Provides parallel primitives, such as scan, sort       | Custom kernel building blocks                          |

## `rocBLAS/hipBLASLt` - Dense `Linear Algebra`[^2]

### What it Does

- Vector - Vector $\textemdash$ AXPY, DOT, SCAL, NRM2
- Matrix - Vector $\textemdash$ GEMV, TRSV
- Matrix - Matrix $\textemdash$ GEMM, TRSM

> [!NOTE] General Matrix Multiplication  
$\text{GEMM}: D = \alpha \times A \times B + \beta \times C$

### Why it is Fast

- Calls MFMA matrix engine
- Tile sizes are selected per CDNA generation to maximize data reuse in LDS and saturate the MFMA engines
- Software pipeline depth is tuned to hide memory latency behind compute and keep the MFMA units busy

## `MIOpen` - Deep Learning Primitives

### Operations

- Convolution $\textemdash$ forward + backward, 2D / 3D, multi-algo  
- Batch norm $\textemdash$ training and inference modes  
- Pooling $\textemdash$ max / average, with optional indices  
- Activations $\textemdash$ `ReLU`, `GELU` (via graph API)  
- `RNN` / `LSTM` / `GRU` $\textemdash$ fused recurrent cells  
- Softmax $\textemdash$ fast, accurate, and log-softmax

### Features

- Multi-algorithm dispatch $\textemdash$ Example: Winograd, `GEMM`, direct, implicit-GEMM - picked per shape
- Two-tier autotune $\textemdash$ `FindDb` chooses algorithm, `PerfDb` tunes its parameters
- Multi-precision $\textemdash$ `fp32`, `fp16`, `bf16`, `int8`
- Operator fusion $\textemdash$ conv + bias + activation in a single kernel

> [!TIP] Why fuse matters
> - Without Fuse $\textemdash$ conv → HBM → bn → HBM → relu
> - With Fuse $\textemdash$ conv + bn + relu (reduces off chip memory access, avoids kernel launch overhead)

### `MIOpen` Autotune

> [!QUESTION] `FindDb` $\textemdash$ Which Solution should be used?  
> Remembers the best MIOpen implementation for a convolution problem.

> [!QUESTION] `PerfDb` $\textemdash$ How should it be tuned?  
> Remembers low-level kernel tuning choices, such as tile size or block size.  

> [!QUESTION] `Kernel cache` $\textemdash$ Is the GPU code already compiled?  
> Reuses compiled GPU kernels to avoid recompilation.

![[c_rocm_e_7.svg]]

## `rocFFT` - Fast `Fourier Transforms`

$$\text{Time Domain} \longleftrightarrow \text{Frequency Domain}$$

### What it Supports

- 1D / 2D / 3D $\textemdash$ arbitrary lengths
- Real & Complex FFTs $\textemdash$ R2C / C2R / C2C
- Batched FFTs $\textemdash$ process $N$ signals at once
- Precisions $\textemdash$ FP16 / FP32 / FP64

### Where You Use it

- Signal processing $\textemdash$ audio, radar, telecom
- Physics simulations $\textemdash$ fluid dynamics, electromagnetics
- Medical imagining $\textemdash$ MRI reconstruction

## `rocSOLVER` - Linear Algebra Decompositions

Here is the information from the rocSOLVER linear algebra decompositions graphic formatted into a Markdown table:

| **Decomposition** | **Equation**                   | **Reveals**                                                                     | **Solves**                                                             |
| ----------------- | ------------------------------ | ------------------------------------------------------------------------------- | ---------------------------------------------------------------------- |
| **LU**            | $A = L \cdot U$                | Lowerand upper-triangular factors.                                              | General linear systems $A \cdot x = b$.                                |
| **Cholesky**      | $A = L \cdot L^T$              | For SPD matrices: only one triangle needs storing. Half the work of LU.         | Symmetric pos-def systems $\cdot$ normal eqns $\cdot$ GPs.             |
| **QR**            | $A = Q \cdot R$                | Q has orthonormal columns ($Q^T Q = I$). Stable solving without inverses.       | Least squares $\cdot$ regression $\cdot$ over-determined systems.      |
| **SVD**           | $A = U \cdot \Sigma \cdot V^T$ | Singular values in $\Sigma$ rank importance. Drop the small ones ~ compression. | PCA $\cdot$ low-rank approx $\cdot$ recommenders $\cdot$ denoising.    |
| **Eigenvalue**    | $A \cdot v = \lambda \cdot v$  | Special directions $v$ that $A$ only stretches. $\lambda$ = stretch factor.     | Spectral analysis $\cdot$ PageRank $\cdot$ stability $\cdot$ dynamics. |

## `rocRAND` - Pseudo Vs Quasi-random Generators

### `PRNG` - Pseudo-random

> [!INFO] Goal  
> Look random and statistically independent enough for simulation.

> [!NOTE]  
> Deterministic algorithm + seed -> reproducible sequence that passes statistical randomness tests.

![[c_rocm_e_8.svg]]  
/// caption  
clustered $\textemdash$ has gaps  
///

- `XORWOW` $\textemdash$ xorshift; fast, simple bit ops
- `MT19937` $\textemdash$ Mersenne Twister
- `MTGP32` $\textemdash$ MT variant tuned for GPUs
- `Philox` $\textemdash$ counter-based, parallel-friendly
- `MRG32K3A` / `MRG31K3P` $\textemdash$ combined multiple recursive
- `LFSR113` $\textemdash$ linear-feedback shift register
- `ThreeFry` $\textemdash$ counter-based, Threefish cipher

> [!INFO] Best for
> - Simulation
> - Sampling
> - Randomized algorithms
> - Stochastic ML kernels

### `QRNG` - Quasi-random

> [!INFO] Goal  
> Fill the space uniformly (low discrepancy).

> [!NOTE]  
> Points are constructed to reduce gaps and clumping. No seed like PRNG - indexed by dimension and offset.

![[c_rocm_e_9.svg]]  
/// caption  
uniform $\textemdash$ no clumping  
///

- `Sobo132` $\textemdash$ 32-bit Sobol low-discrepancy
- `Sobo164` $\textemdash$ 64-bit; higher-resolution output
- Scrambled `Sobo132` $\textemdash$ scrambled for randomization; with low discrepancy
- Scrambled `Sobo164` $\textemdash$ scrambled 64-bit variant

> [!INFO] Best for
> - Quasi-Monte Carlo
> - Numerical Integration
> - Ray Tracing
> - Finance
> - Option Pricing

## `rocSPARSE` - Sparse Matrix Operations

> [!INFO] Core Operations
> - `SpMV`
> - `SpMM`
> - `SpGEMM`
> - `SDDMM`
> - `Sparse solves`
> - `Format conversion`

Here is the information from the storage formats graphic formatted into a Markdown table:

| **Format** | **Description**                                                                   |
| ---------- | --------------------------------------------------------------------------------- |
| **CSR**    | `Compressed Sparse Row` $\textemdash$ most common $\textemdash$ fast `SpMV`       |
| **CSC**    | `Compressed Sparse Column` $\textemdash$ column-oriented operations               |
| **COO**    | `Coordinate list` $\textemdash$ easy to assemble, sort, and convert               |
| **ELL**    | Fixed-width $\textemdash$ best when row sizes are uniform                         |
| **BSR**    | `Block Sparse Row` $\textemdash$ for dense sub-blocks (e.g. FEM)                  |
| **HYB**    | `Hybrid ELL` + `COO` $\textemdash$ reg. rows in `ELL`, `irreg`. overflow in `COO` |

> [!EXAMPLE] Memory Saved Example  
> $10,000 \times 10,000$ `matrix`, $0.1\%$ density (typical `GNN` adjacency)
> - Dense (`fp32`): <span style="color: red;">400 MB</span>
> - `CSR` sparse: $\approx$ <span style="color: cyan;">840 MB</span>  
> $\approx475\times$ smaller and only non zeroes are touched in compute.

## `rocPRIM` / `hipCUB` - Parallel Primitives

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

Here is the comparison matrix for the development approaches shown in the slide:

| **Feature / Aspect**        | **ROCm Libraries**                                                   | **Triton**                                                   | **Raw HIP**                                                     |
| --------------------------- | -------------------------------------------------------------------- | ------------------------------------------------------------ | --------------------------------------------------------------- |
| **Technology / Stack**      | Pre-built library functions (`rocBLAS`, `MIOpen`, `hipBLASLt`, etc.) | Python DSL (`@triton.jit`) for custom kernels with less code | HIP C++ kernels compiling via `amdclang/LLVM` to AMD GPU binary |
| **Usage Example**           | `#!python torch.matmul(a, b)`                                        | Fused, custom, portable kernels                              | Low-level C++ code                                              |
| **Advantages**              | Easiest path for standard operations                                 | Flexible path for custom kernels                             | Maximum low-level control                                       |
| **Trade-offs / Challenges** | Limited flexibility for custom kernel fusion                         | Still requires GPU-kernel thinking                           | Most code and tuning effort required                            |

> [!TIP] Why use `Triton`
> - `Python` Kernel `DSL` $\textemdash$ Write block-level logic; Triton compiles it for the GPU
> - Portable across vendors $\textemdash$ Same source can target AMD and NVIDIA backends; tuning may differ.
> - Auto tuning built in $\textemdash$ `@triton.autotune` benchmarks supplied configs and select best one for a shape.
> - Used by `torch.compile` $\textemdash$ `torch.compile` uses `TorchInductor`; on AMD GPUs `Triton` is a key GPU codegen path.

## `PyTorch` On `ROCm` - Familiar Workflows and Ecosystem

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

- `vLLM`, `SGLang`, `TGI` - OpenAl-compatible APIs  
- `KV-cache` management, continuous batching  
- `FP8` `GEMM` paths on `CDNA 3` and newer  
- Large throughput gains vs naive serving

#### Research

- Rapid prototyping with standard `PyTorch` workflows
- Lightning, Hydra, `W&B`, Diffusers, `HF`

## How `#!python torch.compile()` Optimizes `PyTorch`

### Without `#!python torch.compile()` $\textemdash$ Eager Mode

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

## `RCCL` - Multi-gpu and Multi-node Communication

![[c_rocm_e_13.svg]]  
/// caption  
All Reduce  
///

| **Before**              | **After**            |
| ----------------------- | -------------------- |
| Every GPU has 1 element | Every GPU has $\sum$ |

> [!NOTE]  
> - Each GPU contributes a same-size array
> - All receive the reduced array

> [!TIP] Used in  
> Data-parallel training (gradient sync)

---

![[c_rocm_e_14.svg]]  
/// caption  
All Gather  
///

| **Before**              | **After**                    |
| ----------------------- | ---------------------------- |
| Every GPU has 1 element | every GPU has the full array |

> [!NOTE]
> - Each GPU contributes 1 chunk
> - All receive the concatenated array

> [!TIP] `FSDP` / `ZeRO-3` (gather sharded parameters)

---

![[c_rocm_e_15.svg]]  
/// caption  
Reduce Scatter  
///

| **Before**          | **After**                  |
| ------------------- | -------------------------- |
| Each has full array | Each holds 1 reduced chunk |

> [!NOTE]
> - Reduce across GPUs
> - Each receives 1 reduced chunk

> [!TIP] `FSDP` / `ZeRO-3` (reduce and shard gradients)

---

![[c_rocm_e_16.svg]]  
/// caption  
Broadcast  
///

| **Before**         | **After**         |
| ------------------ | ----------------- |
| Only 1 GPU has `a` | All GPUs have `a` |

> [!NOTE] 
> - One GPU provides an array
> - All receive the same array

> [!TIP] Initial parameter / state sync

---

![[c_rocm_e_17.svg]]  
/// caption  
All to All  
///

| **Before**        | **After**              |
| ----------------- | ---------------------- |
| Each has 2 chunks | Grouped by destination |

> [!NOTE] Each GPU contributes 1 chunk per destination and receives 1 from each destination

> [!TIP] `MoE` token routing (tokens → expert GPU)

## `PyTorch` And `vLLM` for Inference on `ROCm`

> [!INFO]
> - `PyTorch` provides the model framework
> - `vLLM` uses it within a specialized `LLM` inference and serving engine.

### Direct `PyTorch` Inference

- General-purpose $\textemdash$ `LLMs` and other model types
- Flexible execution $\textemdash$ direct control over model and pipeline
- Custom workflows $\textemdash$ preprocessing, logic, and outputs
- Simple deployment $\textemdash$ scripts, applications, or services

### `vLLM` Inference & Serving

- PagedAttention $\textemdash$ manages KV cache in page-like blocks
- Continuous batching $\textemdash$ dynamically batches active requests
- Quantization $\textemdash$ lower precision reduces memory use
- integrates with compatible clients $\textemdash$ OpenAI-compatible API

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