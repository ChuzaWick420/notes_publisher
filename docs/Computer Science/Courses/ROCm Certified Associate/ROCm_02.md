---
Provider: AMD
Platform: AMD AI Developer Program, AMD AI Academy
---

# 2. Architecture

<span style="color: gray;">Dated: 03-10-2026</span>

## `AMD` Instinct Lineage

| **Name**  | **Generation** | **Year** | **Features**           |
| --------- | -------------- | -------- | ---------------------- |
| MI25/MI50 | GCN            | 2017-18  | vector compute begins  |
| MI100     | CDNA 1         | 2020     | first matrix cores     |
| MI200     | CDNA 2         | 2021     | multi-die, strong FP64 |
| MI300/325 | CDNA 3         | 2023-24  | 3D chiplets, FP8       |
| MI350/355 | CDNA 4         | 2025     | FP6/FP4                |
| MI400     | CDNA Next      | H2 2026  | HBM4, UALink, 2nm      |

---

## Specs and Performance by Generation

| **Name**     | **Memory**   | **Bandwidth** | **Performance (FP8 / FP4)**                        |
| ------------ | ------------ | ------------- | -------------------------------------------------- |
| MI300X       | 192 GB HBM3  | 5.3 TB/s      | $\approx$ 5.2 PFLOPS FP8                           |
| MI325X       | 256 GB HBM3E | 6.0 TB/s      | $\approx$ 5.2 PFLOPS FP8                           |
| MI350/355X   | 288 GB HBM3E | 8.0 TB/s      | $\approx$ 10 PFLOPS FP8<br>$\approx$ 20 PFLOPS FP4 |
| MI400 family | 432 GB HBM4  | 19.6 TB/s     | $\approx$ 20 PFLOPS FP8<br>$\approx$ 40 PFLOPS FP4 |

> [!NOTE] PFLOPS listed as peak values with sparsity.

---

## MI300X Package

### Full Package

![[c_rocm_e_4.svg]]  
/// caption  
Package = 8 XCDx + 8 HBM3 stacks (24 GB capacity each) + PCIe + Infinity Fabric + Infinity Cache (256 MB)  
///

---

### One `XCD`

Accelerator Complex Die (`XCD`) = 38 Compute Unites (`CUs`) + `L2` (4 MB - shared by die's `CUs`)

---

### One `CU`

Compute Unit (`CU`) = 4 `SIMDs` (Single Instruction Multiple Data - 16 ALU lanes each) + MFMA (Matrix Fused Multiple-Add) engine (4 per `CU` - 1 per `SIMD`) + Scalar unit + `LDS` (Local Data Share - 64 KB - shared my all threads - programmer managed) + Register file + `L1` (hardware managed - 32 KB)

---

## `MFMA`

The matrix engine computes a full multiply accumulate tile $D = A \times B + C$ in a single instruction.  
The engine comes in different tile shapes ($16 \times 16$ or $32 \times 32$).

> [!NOTE] Note  
> 
> $D = A \times B + C$  
> Here $A$ and $B$ are $16 \times 16$ times and $C$ is accumulator.  
> Instruction: `V_MFMA_F32_16x16x16_F16`
> 
> - FP16 (16 bit floating point) inputs
> - FP32 (32 bit floating point) accumulate

---

## Memory Hierarchy

| **Location**                               | **Capacity**                    | **Bandwidth** | **Speed**                 |
| ------------------------------------------ | ------------------------------- | ------------- | ------------------------- |
| Vector General Purpose Registers (`VGPRs`) | 256 `VGPRs` per thread          | ~100s of TB/s | ~0 cycles                 |
| LDS                                        | 64 KB per `CU`                  | ~10s of TB/s  | ~10s of cycles            |
| L1 Cache                                   | 32 KB per `CU`                  | ~10s of TB/s  | ~10s of cycles            |
| L2 Cache                                   | 4 MB per `XCD` (32 MB in total) | ~34 TB/s      | ~100s of cycles           |
| Infinity Cache                             | 256 MB                          | ~17 TB/s      | ~100s of cycles (> `L2`)  |
| HBM                                        | 192 GB                          | ~5.3 TB/s     | ~100s of cycles (slowest) |

---

## Kernel

A function written to execute on the GPU. When the host program launches the kernel, it creates thousands of threads that process different data in parallel.

---

## `SPMD`

Single Program, Multiple Data - the same kernel runs across many threads at once, each on its own data. It's the model you write in.

> [!EXAMPLE]- Vector Addition  
> `thread i -> c[i] = a[i] + b[i]`
> 
> $$
> \begin{aligned}
> 	\text{thread 0} \to c[0] &= a[0] + b[0] \\
> 	\text{thread 1} \to c[1] &= a[1] + b[1] \\
> 	\text{thread 2} \to c[2] &= a[2] + b[2] \\
> 	&\vdots\\
> 	\text{thread n} \to c[n] &= a[n] + b[n] \\
> \end{aligned}
> $$

---

## Mapping Threads to Chip

- Grid → array of blocks
- Block → up to 1024 threads
- Wavefront → 64 threads executed in lockstep on hardware
- 16 threads per cycle on 1 SIMD - 4 cycles = 1 wavefront executed in lockstep

---

## `SIMT` (Single Instruction, Multiple threads) - `GPU` Execution Model

> [!NOTE] `SIMT`
> - 1 instruction issued to 1 wavefront.
> - 64 threads execute at once with their own data and registers.
> - 64 threads share same `program counter` for lockstepping

> [!TIP]
> - `SPMD` - Programming Model
> - `SIMT` - Execution Model
> - `SIMD` - Hardware Model

---

## Latency Hiding

![[c_rocm_e_5.svg]]  
///caption  
3 wavefronts running on single `SIMD`.  
///

> [!NOTE] Each `CDNA3` `CU` can keep 32 wavefronts in flight.

---

## Architecture Comparison

- `CDNA` for data centers.
- `RDNA` for professional, consumer compute and graphics.

| **Feature / Property**  | **CDNA – AMD Instinct™**      | **RDNA – AMD Radeon™**                          |
| ----------------------- | ----------------------------- | ----------------------------------------------- |
| **Focus**               | Data-center AI and HPC        | Workstation AI and Graphics                     |
| **Graphics hardware**   | None                          | Rasterizers, ray tracing units, display outputs |
| **Matrix acceleration** | MFMA (dedicated matrix cores) | WMMA (AI accelerators)                          |
| **Memory**              | HBM                           | GDDR                                            |
| **Wavefront**           | 64 threads                    | 32 threads                                      |
| **gfx code examples**   | gfx90a, gfx942, gfx950        | gfx1100, gfx1201                                |
| **GPU examples**        | MI250X, MI300X, MI355X        | Radeon RX 7900 XTX, Radeon AI Pro R9700         |

| **Feature / Property** | **Radeon AI Pro R9700 (RDNA 4 · workstation AI)** | **Instinct MI355X (CDNA 4 · data-center AI & HPC)** |
| ---------------------- | ------------------------------------------------- | --------------------------------------------------- |
| **Memory**             | 32 GB GDDR6                                       | 288 GB HBM3E                                        |
| **Bandwidth**          | 640 GB/s                                          | 8 TB/s                                              |
| **FP16 (matrix)**      | 191 TFLOPS                                        | 2.5 PFLOPS                                          |
| **Scales to**          | multiple cards over PCIe                          | 8-GPU nodes - Infinity Fabric                       |
