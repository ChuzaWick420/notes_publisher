---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-10
---

<span style="color: gray;">Dated: 10-11-2024</span>

# More Applications

## Radioactive Decay

Many radioactive materials disintegrate at a rate proportional to the amount present.  
if $A(t)$ is the amount of radioactive substance present at time $t$ then  

$$\frac{dA}{dt}=kA$$

Where $k$ is the constant of proportionality.  
If $A_0$ is the initial amount then using the `population growth rate model`,[^1] we have  

$$A(t) = A_0e^{kt}$$

The `half life` of radio active substance is the time it takes for half of the atoms present to decay.  
if $T$ is the `half life` then  

$$A(T) = \frac {A_0} 2$$

$$\frac{A_{0}}{2}=A_{0}e^{kt}$$

$$kT=-\ln 2$$

### Example

A radio active isotope has half life of $16$ days.  
We have $30g$ of it remaining at the end of $30$ days.  
How much of it was initially present?

#### Solution

Let the amount present at time $t$ be $A(t)$ and initial amount be $A_0$.  

$$\frac{dA}{dt}=kA, \quad A(30)=30$$

$$A(t)=A_{0}e^{kt}$$

$$kT = - \ln 2$$

$$k = - \frac {\ln 2} T$$

$$k = - \frac {\ln 2}{16}$$

$$30=A_{0}e^{30k}$$

$$A_{0}=30e^{-30k}=30e^{\frac{30\ln 2}{16}}=110.04 g$$

## Newton's Law of Cooling

Temperature $T(t)$ of a body changes at a rate proportional to the difference between the temperature in the body and the temperature $T_m$ of its surroundings.  
This is called `Newton's law of cooling`.  

$$\frac{dT}{dt}=k(T-T_{m}), \quad T(0)=T_{0}$$

$$\int\frac{dT}{T-T_{m}}=\int k~dt$$

$$\ln|T-T_{m}|=kt+C$$

$$T-T_{m}=e^{kt+C}$$

$$T(t)=T_{m}+C_{1}e^{kt}$$

$$\because T(0) = T_0$$

$$\therefore C_1 = T_0 - T_m$$

$$T(t)=T_{m}+(T_{0}-T_{m})e^{kt}$$

If we have temperature known at $t_1$ and $t_2$ then  

$$\because T(t)=T_{m}+(T_{0}-T_{m})e^{kt}$$

$$\implies T(t_{1})-T_{m}=(T_{0}-T_{m})e^{kt_{1}} \text{ and } T(t_{2})-T_{m}=(T_{0}-T_{m})e^{kt_{2}}$$

$$\frac{T(t_{1})-T_{m}}{T(t_{2})-T_{m}}=e^{k(t_{1}-t_{2})}$$

### Example

Suppose that a dead body was discovered at midnight when its temperature was $80^\circ F$.  
The room temperature is kept constant at $60^\circ F$.  
Two hours later, the body temperature drops to $75^\circ F$.  
Find the time of death.

#### Solution

Assuming that the person was not sick. Therefore,  

$$T(0) = 98.6^\circ F = T_0$$

$$T_m = 60^\circ F$$

$$\frac{dT}{dt}=k(T-60), \quad T(0)=98.6$$

$$T(t)=T_{m}+(T_{0}-T_{m})e^{kt}$$

$$\frac{T(t_{1})-T_{m}}{T(t_{2})-T_{m}}=e^{k(t_{1}-t_{2})}$$

$$T(t_{1})=80^{\circ}F \text{ and } T(t_{2})=75^{\circ}F$$

$$\because t_1 - t_2 = 2 \text{ hours}$$

$$\frac{80-60}{75-60}=e^{2k}$$

$$k=\frac{1}{2}\ln\frac{4}{3}=0.1438$$

For the time of death, we need to find the `interval`[^2] $t_1 - t_2 = t_d$.  

$$\frac{T(t_{1})-T_{m}}{T(t_{2})-T_{m}}=e^{k(t_{1}-t_{2})} \implies \frac{98.6-60}{80-60}=e^{kt_{d}}$$

$$t_{d}=\frac{1}{k}\ln\frac{38.6}{20} \approx 4.573$$

Hence the time of death is $7:42 PM$.

## Carbon Dating

`Carbon-14` is produced in the atmosphere through cosmic radiation acting on nitrogen, maintaining a constant ratio with ordinary carbon.  
Living organisms contain the same proportion of `C-14` as the atmosphere, but once they die, they stop absorbing it.  
By comparing `C-14` levels in a fossil to atmospheric levels, scientists can estimate its age.  
This method, which relies on `C-14`'s half-life of about 5600 years, has been used to date artifacts, such as ancient Egyptian furniture.

### Example

A fossilized bone is found to contain $\frac 1 {1000}$ of the original amount of `C-14`.  
Determine the age of the fissile.

#### Solution

$$\frac{dA}{dt}=kA, \quad A(0)=A_{0}$$

$$A(t)=A_{0}e^{kt}$$

The `half life` of carbon isotope is $5600$ years.  

$$A(5600)=\frac{A_{0}}{2}$$

$$\frac{A_{0}}{2}=A_{0}e^{5600k}$$

$$k = −0.00012378$$

$$A(t)=A_{0}e^{-(0.00012378)t}$$

$$\because A(t) = \frac{A_0}{1000}$$

$$\frac{A_{0}}{1000}=A_{0}e^{-(0.00012378)t} \implies -0.00012378t=-\ln 1000$$

$$t=\frac{\ln (1000)}{0.00012378}=55,800 \text{years}$$

## References

Read more about [[Mathematics/Mathematical notations/Content|notations and symbols]].

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 5/MTH401 - Differential Equations/10. Applications of First Order Differential Equations/Lecture|population growth rate model]].
[^2]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].