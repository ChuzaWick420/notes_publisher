---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-10-30
---

<span style="color: gray;">Dated: 30-10-2024</span>

# `Functions`[^1] With `Periods`[^2] other than $2 \pi$

There are sometimes `functions`[^1] which have $T$ `period`[^2] which is other than $2 \pi$.  
We know that in physics, the oscillations are basically `function`[^1] of `time` and they repeat after $T$ interval.  

$$f(t) = f(t + T)$$

If the `frequency` measured in `hertz` (Hz) is defined as  

$$f = \frac 1 T$$

and `angular velocity` as  

$$\omega = 2 \pi f$$

then  

$$\omega = \frac {2 \pi}{T} \implies 2 \pi = \omega \cdot T$$

therefore, the `angle` $x$ at any given time $t$ will be  

$$x = \omega \cdot t$$

The `fourier series`[^3] takes the form

$$f(t) = \frac 1 2 a_0 + \sum_{n = 1}^\infty \left(a_n \cos(n \omega t) + b_n \sin(n \omega t)\right)$$

## Fourier Coefficients

$$a_{0}=\frac{2}{T}\int_{0}^{T}f(t)dt=\frac{\omega}{\pi}\int_{0}^{ \frac {2\pi}\omega}f(t)dt$$

$$a_{n}=\frac{2}{T}\int_{0}^{T}f(t)\cos(n\omega t)dt=\frac{\omega}{\pi}\int_{0}^{\frac{2\pi}\omega}f(t)\cos(n\omega t)dt$$

$$b_{n}=\frac{2}{T}\int_{0}^{T}f(t)\sin(n\omega t)dt=\frac{\omega}{\pi}\int_{0}^{\frac{2\pi}\omega}f(t)\sin(n\omega t)dt$$

## Half Wave Rectifier

A `sinusoidal` voltage $E \sin (\omega t)$ is passed through a `half wave rectifier` which clips the negative voltage onto the $x$ axis.  
Find the `fourier series`[^3] for the resulting `periodic function`.  

$$u(t) = 0 \quad - \frac T 2 < t < 0$$

$$u(t) = E \sin (\omega t) \quad 0 < t < \frac T 2$$

### Solution

#### $a_0$

$$a_{0}=\frac{2}{T}\int_{- \frac {T}2}^{\frac T 2}u(t)dt$$

$$=\frac{2}{T}\left(\int_{- \frac T 2}^{0}0~dt+\frac{E}{T}\int_{0}^{\frac T 2}\sin(\omega t)dt\right)$$

$$=\frac{2E}{T^{2}}\left[-\frac{1}{\omega}\cos(\omega t)\right]_{0}^{\frac T 2}$$

$$=\frac{2E}{\pi\omega}\left(1-\cos~\frac{\pi\omega T}{2}\right)$$

$$=\frac{\omega}{\pi}E\left|\frac{-\cos~\omega~t}{\omega}\right|_{0}^{\frac \pi \omega}$$

$$=\frac{2E}{\pi}$$

#### $a_1$

$$a_{n}=\frac{2}{T}\int_{\frac T 2}^{\frac T 2}u(t)\cos(n\omega t)dt$$

$$=\frac{2E}{T}\int_{0}^{\frac T 2}\sin(\omega t)\cos(n\omega t)dt$$

$$=\frac{\omega E}{2\pi}\int_{0}^{\frac {2\pi}\omega}2\sin(\omega t)\cos(n\omega t)dt$$

$$=\frac{\omega E}{2\pi}\int_{0}^{\frac \pi \omega}(\sin(1+n)\omega t+\sin(1-n)\omega t)dt$$

$$
a_n = \frac{\omega E}{2\pi} \left[ -\frac{\cos (1+n) \, \omega t}{(1+n) \omega} - \frac{\cos (1-n) \, \omega t}{(1-n) \omega} \right]_{0}^{\frac{\pi}{\omega}}
$$

$$
= \frac{\omega E}{2\pi} \left[ -\frac{\cos (1+n) \, \pi + 1}{(1+n)\omega} + \frac{-\cos (1-n) \, \pi + 1}{(1-n)\omega} \right]
$$

$$
= \frac{\omega E}{2\pi \omega} \left[ \frac{-\cos (1+n) \, \pi + 1}{(1+n)} + \frac{-\cos (1-n) \, \pi + 1}{(1-n)} \right]
$$

##### If $n$ is Odd

$$a_n = 0$$

##### If $n$ is even

$$a_n = \frac{E}{2\pi} \left( \frac{2}{1+n} + \frac{2}{1-n} \right) $$

$$= \frac{E}{2\pi} \left[ \frac{2 - 2n + 2 + 2n}{(1+n)(1-n)} \right] $$

$$= \frac{2E}{(1-n)(1+n)\pi}$$

$$
= \frac{2E}{(1-n^2)\pi}
$$

#### $b_n$

$$b_{n}=\frac{2}{T}\int_{-\frac T 2}^{\frac T 2}u(t)\sin(n\omega t)dt$$

$$=\frac{2E}{T}\int_{0}^{\frac T 2}\sin(\omega t)\sin(n\omega t)dt$$

$$=\frac{\omega E}{2\pi}\int_{0}^{\frac {2\pi}\omega}2\sin(\omega t)\sin(n\omega t)dt$$

$$=\frac{\omega E}{2\pi}\int_{0}^{\frac \pi \omega}\left(\cos(1+n)\omega t-\cos(1-n)\omega t\right)dt$$

##### If $n = 1$

$$b_n = - \frac{\omega E}{2 \pi} \int_0^{\frac \pi \omega} (\cos (2 \omega t) - 1)dx$$

$$= - \frac{\omega E}{2 \pi} \left|\frac{\sin (2 \omega t)}{2 \omega} - 1\right|_0 ^ {\frac \pi \omega}$$

$$= - \frac{\omega E}{2 \pi} \left(- \frac \pi \omega\right)$$

$$= \frac E 2$$

##### If $n \ne 1$

$$=-\frac{\omega E}{2\pi}\left[\frac{\sin(1+n)\omega t}{(1+n)\omega}-\frac{\sin(1-n)\omega t}{(1-n)\omega}\right]_{0}^{\frac \pi \omega}$$

$$=-\frac{\omega E}{2\pi}\left[\frac{\sin(1+n)\pi}{(1+n)\omega}-\frac{\sin(1-n)\pi}{(1-n)\omega}\right]$$

$$= 0$$

$$u(t)=\frac{1}{2}a_{0}+\sum_{n=2}^{\infty}a_{n}\cos(n\omega t)$$

$$u(t)=\frac{E}{\pi}+\frac{E}{2}\sin(\omega t)-\frac{2E}{\pi}\left(\frac 1 {1.3} \cos (2 \omega t) + \frac 1 {3.5} \cos (4 \omega t)+ \ldots\right)$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[Mathematics/Function/Content|functions]].
[^2]: Read more about [[semester 2/MTH301 - Calculus II/39. Periodic Functions/Lecture|periodic functions]].
[^3]: Read more about [[semester 2/MTH301 - Calculus II/40. Fourier Series/Lecture|fourier series]].