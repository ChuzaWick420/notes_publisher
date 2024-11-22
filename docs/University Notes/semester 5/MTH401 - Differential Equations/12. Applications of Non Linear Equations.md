---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-15
---

<span style="color: gray;">Dated: 15-11-2024</span>

# Application of Non Linear Equations

## Logistic Equation

The `logistic model` is also called `Verhulst-Pearl model`.  
Suppose $a > 0$ is the constant average rate of birth and that death rate is proportional to the population $P(t)$ at any time $t$.  
Thus if $\frac 1 P \cdot \frac {dP}{dt}$ is the rate of growth per individual then

$$
\frac{dP}{dt} = P(a-bP)
$$

The term $-bP^2$ where $b > 0$ can be interpreted as inhibition term.  
When $b = 0$ then the equation reduces to the one in `exponential model`.[^1]

### Solution to Logistic Equation

For the constant solutions  

$$P (a - bP) = 0$$

$$\implies P = \frac a b$$

For non constant solutions, 

$$
\frac{dP}{P(a-bP)} = dt
$$

Resolve into `partial fractions`,[^2] we have

$$
\left[\frac{\frac 1 a}{P} + \frac{\frac b a}{a-bP}\right] dP = dt
$$

$$
\frac{1}{a}\ln|P|-\frac{1}{a}\ln|a-bP|=t+C
$$

$$
\ln\left|\frac{P}{a-bP}\right|=at+aC
$$

$$
\frac{P}{a-bP} = C_{1}e^{at} \quad \text{where } C_1 = e^{aC}
$$

$$
P(t)=\frac{aC_{1}e^{at}}{1+bC_{1}e^{at}}=\frac{aC_{1}}{bC_{1}+e^{-at}}
$$

If we are given any initial value problem such that  

$$P(0) = P_0, \quad P_0 \ne \frac a b$$

We get 

$$
C_{1}=\frac{P_{0}}{a-bP_{0}}
$$

Plugging it back in, we get

$$
P(t)=\frac{aP_{0}}{bP_{0}+(a-bP_{0})e^{-at}}
$$

It is clear that there is limited growth as $t \to \infty$.

$$
\lim_{t\rightarrow\infty}P(t)=\frac{aP_{0}}{bP_{0}}=\frac{a}{b}
$$

## Special Cases of Logistic Equation

### Epidemic Spread

Suppose that one person infected from a contagious disease is introduced in a fixed population of $n$ people.

> [!NOTE]- Assumption  
> Rate of spread of disease $\frac {dx}{dt}$ is proportional to number of infected people $x(t)$ and number of uninfected people $y(t)$.

$$\frac {dx}{dt} = kxy$$

$$x + y = n + 1$$

Therefore, 

$$
\frac{dx}{dt}=kx(n+1-x), \quad x(0)=1
$$

This is used for

- Spread of information
- Impact of advertising

### Modification of Logistic Equation

$$
\frac{dP}{dt}=P(a-b\ln P)
$$

This equation is used in studies of

- Solid tumors
- Actuarial Predictions
- Growth of revenue from the sale of a commercial product
- Growth or decline of population

#### Example

A flu virus spreads on a college campus of 1000 students at a rate proportional to the product of infected ($x$) and uninfected students $(1000 - x)$.  
If $x(4) = 50$, determine the number of infected students after $6$ days.

##### Solution

$$
\frac{dx}{dt}=kx(1000-x), \quad x(0)=1
$$

$$a = 1000k \text { and } b = k$$

Therefore, the solution is

$$
P(t)=\frac{aP_{0}}{bP_{0}+(a-bP_{0})e^{-at}}
$$

$$
x(t)=\frac{1000k}{k+999ke^{-1000kt}}=\frac{1000}{1+999e^{-1000kt}}
$$

Now using $x(4) = 50$, we determine $k$.

$$
50=\frac{1000}{1+999e^{-4000k}}
$$

$$
k=\frac{-1}{4000}\ln\frac{19}{999}=0.0009906
$$

$$
x(t)=\frac{1000}{1+999e^{-0.9906t}}
$$

$$
x(6)=\frac{1000}{1+999e^{-5.9436}}=276 \text{ students}
$$

## Chemical Reactions

In a first-order chemical reaction, substance $A$ decomposes into smaller molecules at a rate proportional to the remaining amount of $A$.  
Radioactive decay is an example of this type of reaction.  
If $X$ is the remaining amount of substance $A$ at any time $t$ then  

$$\frac {dX}{dt} = kX$$

$k < 0$ because $X$ is decreasing.  

In a second-order reaction, chemicals $A$ and $B$ react to form chemical $C$ at a rate proportional to the product of their remaining concentrations.  
If $X$ is the amount of $C$ formed at time $t$, the unconverted amounts of $A$ and $B$ are $\alpha - X$ and $\beta - X$, respectively.  
Hence the rate of formation of chemical $C$ is

$$
\frac{dX}{dt}=k(\alpha-X)(\beta-X)
$$

### Example

A compound $C$ forms when chemicals $A$ and $B$ react in a ratio of $1:4$.  
If $30$ grams of $C$ are formed in $10$ minutes, and the reaction rate is proportional to the product of the remaining amounts of $A$ and $B$, determine the amount of $C$ at any time, given initial amounts of $50$ grams of $A$ and $32$ grams of $B$.  
Find $C$ at $15$ minutes and interpret as $t \to \infty$.

#### Solution

If $X(t)$ denotes the number of grams of chemical $C$ present at time $t$, then  

$$X(0) = 0 \text{ and } X(10) = 30$$

Suppose there are $2$ grams of compound $C$ and we have used $\alpha$ grams of $A$ and $b$ grams of $B$ then  

$$a + b = 2 \text{ and } b = 4a$$

Solving these equations, we get  

$$a = 2 \cdot \frac 1 5$$

$$b = 2 \cdot \frac 4 5$$

If there were $X$ amount of $C$ then  

$$a = \frac X 5 \text{ and } b = \frac 4 5 \cdot X$$

Therefore, the amount of $A$ and $B$ remaining at any time $t$ are  

$$50 - \frac X 5 \text{ and } 32 - \frac 4 5 \cdot X$$

Therefore,

$$
\frac{dX}{dt}=\lambda\left(50-\frac{X}{5}\right)\left(32-\frac{4}{5}X\right)
$$

$$
\frac{dX}{dt}=k(250-X)(40-X), \quad k=\frac {4\lambda}{25}
$$

Solving the equation

$$
\frac{dX}{(250-X)(40-X)}=kdt
$$

$$
-\frac{1}{210}\frac{dX}{250-X}+\frac{1}{210}\frac{dX}{40-X}=kdt
$$

$$
\ln\left|\frac{250-X}{40-X}\right|=210kt+c_{1}
$$

$$
\frac{250-X}{40-X}=c_{2}e^{210kt} \quad \text{ where } \quad c_{2}=e^{c_{1}}
$$

When $t = 0$, $X = 0$, so it follows at this point that $c_2 = \frac {25} 4$.  
Using $X = 30$ at $t = 10$, we find

$$
210k=\frac{1}{10}\ln\frac{88}{25}=0.1258
$$

We will solve for $X$

$$
X(t)=1000\left(\frac{1-e^{-0.1258t}}{25-4e^{-0.1258t}}\right)
$$

It is clear that $e^{-0.1258t} \to 0$ as $t \to \infty$.  
Therefore, $X \to 40$ as $t \to \infty$.

| t   | X     |
| --- | ----- |
| 10  | 30    |
| 15  | 34.78 |
| 20  | 37.25 |
| 25  | 38.54 |
| 30  | 39.22 |
| 35  | 39.59 |

$$
50-\frac{1}{5}(40)=42 \text{ grams of chemical } A
$$

$$
32-\frac{4}{5}(40)=0 \text{ grams of chemical } B
$$

## Miscellaneous Applications

### Application 1

The velocity $v$ and a falling mass $m$ subject to air resistance, is given by

$$
m\frac{dv}{dx}=mg-kv
$$

### Application 2

The rate at which a drug disseminates into bloodstream is governed by the differential equation

$$
\frac{dx}{dt}=A-Bx
$$

$x(t)$ describes the concentration of drug in the bloodstream at any time $t$.

### Application 3

The rate of memorization of a subject is given by

$$
\frac{dA}{dt}=k_{1}(M-A)-k_{2}A
$$

$A(t)$ is the amount of material memorized at any time $t$.  
$M$ is the total amount.

## References

Read more about [[M_Notations|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/10. Applications of First Order Differential Equations/Lecture|exponential model]].
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/45. Theorems/Lecture|partial fractions]].