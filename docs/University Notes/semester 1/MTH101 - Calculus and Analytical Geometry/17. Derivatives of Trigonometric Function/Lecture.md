---
tags:
  - university-notes
university-name: Virtual University of Pakistan
---

# Derivative of $f(x) = \sin(x)$

$$\frac{d}{dx} (\sin x) = \lim_{h \to 0} \frac{\sin(x+h) - \sin(x)}{h}$$

$$ = \lim_{h \to 0} \frac{\sin(x)\cos(h) + \cos(x)\sin(h) - \sin(x)}{h}$$

$$ = \lim_{h \to 0} \frac{\sin(x)\cos(h) - \sin(x) + \cos(x)\sin(h)}{h}$$

$$ = \lim_{h \to 0} \left[\sin(x)\left(\frac{\cos(h)-1}{h}\right) + \cos(x)\left(\frac{\sin(h)}{h}\right)\right]$$

$$ = \lim_{h \to 0} \left[\cos(x)\left(\frac{\sin(h)}{h}\right) - \sin(x)\left(\frac{1-\cos(h)}{h}\right)\right]$$

$$\because \lim_{h \rightarrow 0} \cos(x) = \cos(x)$$

$$\because \lim_{h \rightarrow 0} \sin(x) = \sin(x)$$

And both are constants,  

$$ = \cos(x)\lim_{h\to0}\left(\frac{\sin (h)}{h}\right)-\sin(x)\lim_{h\to0}\left(\frac{1-\cos (h)}{h}\right)$$

$$= \cos(x) \cdot (1) - \sin(x) \cdot (0)$$

$$= \cos(x)$$

# Derivative of $f(x) = \cos(x)$

$$\frac{d}{dx}cos(x) = \lim_{h\to0}\frac{cos(x+h)-cos(x)}{h}$$

$$= \lim_{h\to0}\frac{\cos(x)\cos(h)-\sin(x)\sin(h)-\cos(x)}{h}$$

$$= \lim_{h\to0}\left(\frac{\cos(x)\cos(h)-\cos(x)}{h}-\frac{\sin(x)\sin(h)}{h}\right)$$

$$= \lim_{h\to0}\left(\cos(x)\left(\frac{\cos(h)-1}{h}\right)-\frac{\sin(x)\sin(h)}{h}\right)$$

$$= \cos(x)(0) - \sin(x)(1)$$

$$= -\sin(x)$$

# Derivative of $f(x) = \tan(x)$

$$\frac{d}{dx}\tan(x) = \frac{d}{dx}\left[\frac{\sin(x)}{\cos(x)}\right]$$

using the `quotient formula`[^1]  

$$= \frac{\cos(x)\frac{d}{dx}\sin(x)-\sin(x)\frac{d}{dx}\cos(x)}{\cos^{2}(x)}$$

$$= \frac{\cos(x)\cos(x)-\sin(x)[-\sin(x)]}{\cos^{2}(x)}$$

$$= \frac{\cos^{2}(x)+\sin^{2}(x)}{\cos^{2}(x)}$$

$$=\frac{1}{\cos^{2}(x)}$$

$$= \sec^2(x)$$

# Derivative of $f(x) = \sec(x)$

$$\frac{d}{dx}\sec(x) = \frac{d}{dx}\left(\frac{1}{\cos(x)}\right)$$

Using the `quotient formula` [^1]  

$$=\frac{cos(x)(0)-(1)[-sin(x)]}{\cos^{2}(x)}$$

$$=\frac{\sin(x)}{\cos(x)}\cdot\frac{1}{\cos(x)}$$

$$=\sec(x)\tan(x)$$

# Derivative of $f(x) = \csc(x)$

$$\frac{d}{dx}\csc(x) = \frac{d}{dx}\left(\frac{1}{\sin(x)}\right)$$

$$=\frac{\sin(x)(0)-(1)[\cos(x)]}{\sin^{2}(x)}$$

$$=-\frac{\cos(x)}{\sin(x)}\cdot\frac{1}{\sin(x)}$$

$$=-\csc(x)\cot(x)$$

# Derivative of $f(x) = \cot(x)$

$$\frac{d}{dx}\cot(x) = \frac{d}{dx}\left(\frac{1}{\tan(x)}\right)$$

$$=\frac{\tan(x)(0)-(1)[\sec^{2}(x)]}{\tan^{2}(x)}$$

$$=-\frac{\sec^{2}(x)}{\tan^{2}(x)}$$

$$=-\csc^{2}(x)$$

# References

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/16. Techniques of Differentiation/Lecture|Quotient Formula]].
