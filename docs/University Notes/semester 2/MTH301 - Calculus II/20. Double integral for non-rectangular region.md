---
tags:
  - university-notes
  - integral
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# Double `Integral`[^1] for Non Rectangular Region

## Example

Evaluate an equivalent `integral`[^1] of reversed order with respect to  

$$\int_0^2\int_{x^2}^{2x} (4x + 2) dydx$$

$$\text{where } x^2 \le y \le 2x \text{ and } 0 \le x \le 2$$

Reversing the order, we get  

$$\int_{x^2}^{2x}\int_0^2(4x+2)dxdy$$

We want the limits of outer `integral`[^1] to be numeric values so it can yield numeric answers.  
Therefore, from the `inequality`[^2] $x^2 \le y \le 2x$, we got $\frac y 2 \le x \le \sqrt y$  
Putting $x = 0,2$ in the `inequality`[^2] produces $0 \le y \le 4$.  
Hence,  

$$\int_{0}^{4}\int_{\frac y 2}^{\sqrt y}(4x+2)dxdy$$

 Evaluate this and we will get  

$$= 8$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[25. Integrations|integrals]]. 
[^2]: Read more about [[1. Coordinates, Graphs, Lines|inequalities]]. 