---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-08
---

<span style="color: gray;">Dated: 08-11-2024</span>

# Separable Equations

The differential equation  

$$\frac{dy}{dx} = f(x, y)$$

is called `separable equation` if it can be written as 

$$\frac{dy}{dx} = h(x)g(y)$$

To solve `separable equations`, we perform the following steps

- We find $g(y) = 0$ to find constant solutions to the equation.
- For non constant solutions, we write the equation as  

$$\frac{dy}{g(y)}=h(x)dx$$

Then `integrate`[^1] it  

$$\int \frac{1}{g(y)} dy = \int h(x) dx$$

To get the solution of the form  

$$G(y) = H(x) + C$$

- We list the entire constant and non-constant solutions to avoid repetition.
- If you are given `Initial value problem`,[^2] use the initial condition to find the particular solution.

> [!NOTE]- Note
> - No need to use 2 constants of `integration`[^1] because $C_1 - C_2 = C$
> - The constants of `integration`[^1] can be relabeled in a convenient way.
> - Since a particular solution may coincide with a constant solution, step 3 is important.

## Example

$$\frac{dy}{dt}=1+t^{2}+y^{2}+t^{2}y^{2}, y(0)=1$$

$$\because 1+t^{2}+y^{2}+t^{2}y^{2}=(1+t^{2})(1+y^{2})$$

### Step 1

$$1 + y^2 = 0$$

$$\implies y = \pm \sqrt {-1}$$

There are no real solutions

### Step 2

$$\frac{dy}{1+y^{2}}=(1+t^{2})dt$$

$$\int \frac{dy}{1+y^{2}}=\int(1+t^{2})dt$$

$$\tan^{-1}(y)=t+\frac{t^{3}}{3}+C$$

$$y=\tan\left(t+\frac{t^{3}}{3}+C\right)$$

### Step 3

Since there are no real solutions, all solutions are given by implicit and explicit solutions

### Step 4

The initial condition $y(0) = 1$ gives  

$$C=\tan^{-1}(1)=\frac{\pi}{4}$$

Hence the solution to this `initial value problem`[^2] is  

$$\tan^{-1}(y)=t+\frac{t^{3}}{3}+\frac{\pi}{4}$$

$$y=\tan\left(t+\frac{t^{3}}{3}+\frac{\pi}{4}\right)$$

## Example

$$\frac{dy}{dx}=(y-1)^{2}, y(0)=1$$

### Step 1

$$(y - 1)^2 = 0 \implies y = 1$$

### Step 2

$$\frac{dy}{(y-1)^{2}}=dx$$

$$\int(y-1)^{-2}dy=\int dx$$

$$\frac{(y-1)^{-2+1}}{-2+1}=x+c$$

$$-\frac{1}{y-1}=x+c$$

### Step 3

All solutions of the equation are

$$
=
\begin{cases}
	-\frac{1}{y-1}=x+c \\
	y = 1
\end{cases}
$$

### Step 4

$$\because y(0) = 1$$

$$- \frac 1 {y(x) - 1} = x + c$$

$$\because x \to 0$$

$$\implies y(x) - 1 \to 0$$

$$\implies - \frac 1 {y(x) - 1} \to -\infty$$

$$\implies c \to -\infty$$

Plug it back into the equation  

$$- \frac 1 {y - 1} = - \infty$$

$$\frac 1 \infty = y - 1$$

$$\implies y = 1$$

Hence the solution is $y = 1$.

## References

Read more about [[M_Notations|notations and symbols]].

[^1]: Read more about [[25. Integrations|integration]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/2. Fundamentals/Lecture|initial value problem]].