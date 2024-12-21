---
tags:
  - university-notes
university-name: Virtual University of Pakistan
date: 2024-11-05
---

<span style="color: gray;">Dated: 05-11-2024</span>

# Lecture No. 6

John Tukey introduced the Stem-and-Leaf Display in 1977 to address the limitation of frequency tables losing individual observations.  
This display splits each number into a stem (leading digits) and a leaf (trailing digits), separated by a vertical line, allowing simultaneous sorting and visualization of the data.

| Leading Digit | Trailing Digits |
| ------------- | --------------- |
| 2             | 43              |
| Stem          | Leaf            |

OR

| Leading Digit | Trailing Digit |
| ------------- | -------------- |
| 24            | 3              |
| Stem          | Leaf           |

## Example

The ages of 30 hospital patients range from 12 to 74.  
Construct a stem-and-leaf display by using the leading digit as the stem and the trailing digit as the leaf.  
For example, 48 is split into a stem of 4 and a leaf of 8. The data is organized in the order it appears.

| Stem (Leading Digit) | Leaf (Trailing Digit) |
| -------------------- | --------------------- |
| 1                    | 82                    |
| 2                    | 967                   |
| 3                    | 17905                 |
| 4                    | 830289                |
| 5                    | 412378                |
| 6                    | 415278                |
| 7                    | 14                    |

But it is a common practice to arrange the trailing digits in each row from smallest to highest.

| Stem (Leading Digit) | Leaf (Trailing Digit) |
| -------------------- | --------------------- |
| 1                    | 28                    |
| 2                    | 679                   |
| 3                    | 01579                 |
| 4                    | 023889                |
| 5                    | 123478                |
| 6                    | 124578                |
| 7                    | 14                    |

### Frequency Distribution

| Class Limits | Class Boundaries | Frequency |
| :----------: | :--------------: | :-------: |
|   10 - 19    |    9.5 - 19.5    |     2     |
|   20 - 29    |   19.5 - 29.5    |     3     |
|   30 - 39    |   29.5 - 39.5    |     5     |
|   40 - 49    |   39.5 - 49.5    |     6     |
|   50 - 59    |   49.5 - 59.5    |     6     |
|   60 - 69    |   59.5 - 69.5    |     6     |
|   70 - 79    |   69.5 - 79.5    |     2     |

![[Pasted image 20241105194028.png]]

The `x axis` represents age and `y axis` represents number of patients.

### Description of Variable Data

In statistical inquiries, a concise numerical description is preferable to lengthy tables, especially if it helps visualize and interpret the data's significance.

### Measures of Central Tendency and Measures of Dispersion

- Averages enable us to measure the central tendency of variable data
- Measures of dispersion enable us to measure its variability.

#### Averages

An average is a single value that represents a data set or distribution, serving as a central value around which observations cluster.  
It indicates the distribution's position on the X-axis, hence is referred to as a measure of central tendency or location.

##### Example

Looking at these two `frequency distributions`, we should ask ourselves what exactly is the distinguishing feature?  
If we draw the frequency polygon of the two frequency distributions, we obtain  
![[Pasted image 20241105194941.png]]  
The frequency polygons for the two suburbs have the same shape but differ in position relative to the X-axis.  
The mean number of rooms per house is 6.67 in suburb A and 7.67 in suburb B, indicating that, on average, houses in suburb B are larger than those in suburb A by one room.

##### Various Types of Averages

- The arithmetic mean
- The geometric mean
- The harmonic mean
- The median
- The mode

The `Arithmetic`, `Geometric`, and `Harmonic` means are mathematical averages that reflect the magnitude of observed values.  
The `Median` shows the middle position, while the Mode identifies the most frequent value in the data set.  
The `Mode` is the value that occurs most often, representing the most common result.

##### Example

Suppose that the marks of eight students in a particular test are as follows: 2, 7, 9, 5, 8, 9, 10, 9.  
Obviously, the most common mark is 9.  
In other words,  

$$\text{Mode} = 9$$

##### Mode in case of Raw Data of a Continuous Variable

For ungrouped raw data of a continuous variable, the mode is determined by counting the frequency of each value.

##### Example

Suppose that the government of a country collected data regarding the percentages of revenues spent on Research and Development by 49 different companies, and obtained the following figures

| Company | Percentage | Company | Percentage |
| ------- | ---------- | ------- | ---------- |
| 1       | 13.5       | 14      | 9.5        |
| 2       | 8.4        | 15      | 8.1        |
| 3       | 10.5       | 16      | 13.5       |
| 4       | 9.0        | 17      | 9.9        |
| 5       | 9.2        | 18      | 6.9        |
| 6       | 9.7        | 19      | 7.5        |
| 7       | 6.6        | 20      | 11.1       |
| 8       | 10.6       | 21      | 8.2        |
| 9       | 10.1       | 22      | 8.0        |
| 10      | 7.1        | 23      | 7.7        |
| 11      | 8.0        | 24      | 7.4        |
| 12      | 7.9        | 25      | 6.5        |
| 13      | 6.8        | 26      | 9.5        |
| 27      | 8.2        | 39      | 6.5        |
| 28      | 6.9        | 40      | 7.5        |
| 29      | 7.2        | 41      | 7.1        |
| 30      | 8.2        | 42      | 13.2       |
| 31      | 9.6        | 43      | 7.7        |
| 32      | 7.2        | 44      | 5.9        |
| 33      | 8.8        | 45      | 5.2        |
| 34      | 11.3       | 46      | 5.6        |
| 35      | 8.5        | 47      | 11.7       |
| 36      | 9.4        | 48      | 6.0        |
| 37      | 10.5       | 49      | 7.8        |
| 38      | 6.9        |         |            |

###### Dot Plot

A dot plot uses a horizontal axis to represent a quantitative variable, with each data measurement indicated by a dot.  
Repeated values result in stacked dots at the corresponding numerical position.  
![[Pasted image 20241105200459.png]]  
Also, this dot plot shows that 
- almost all of the R&D percentages are falling between 6% and 12%.
- most of the percentages are falling between 7% and 9%.

$$\hat X = 6.9$$

##### Mode in case of Discrete Frequency Distribution

In case of a discrete frequency distribution, identification of the mode is immediate; one simply finds that value which has the highest frequency.

###### Example

| No. of Passengers  X | No. of Flights f |
| -------------------- | ---------------- |
| 28                   | 1                |
| 33                   | 1                |
| 34                   | 2                |
| 35                   | 3                |
| 36                   | 5                |
| 37                   | 7                |
| 38                   | 10               |
| 39                   | 13               |
| 40                   | 8                |
| Total                | 50               |

$$\text{Highest Frequency } f_m = 13$$

$$\text{Occurs against the } X \text{ value} = 39$$

$$\text{Mode } = x = 39$$

##### Mode in case of the Frequency Distribution of a Continuous Variable

$$\text{Mode } = \hat X = 1 + \frac{f_m - f_1}{(f_m - f_1) - (f_m - f_2)} xh$$

$$\text{Where}$$

$$1 = \text{ lower class boundary of the modal class}$$

$$f_m = \text{ frequency of the modal class}$$

$$f_1 = \text{ frequency of the class preceding the modal class}$$

$$f_2 = \text{ frequency of the class following modal class}$$

$$h = \text{length of class interval of the modal class}$$

| Mileage Rating | Class Boundaries | No. of Cars |
| -------------- | ---------------- | ----------- |
| 30.0 - 32.9    | 29.95 - 32.95    | 2           |
| 33.0 - 35.9    | 32.95 - 35.95    | $4 = f_1$   |
| 36.0 - 38.9    | 35.95 - 38.95    | $14 = f_m$  |
| 39.0 - 41.9    | 38.95 - 41.95    | $8 = f_2$   |
| 42.0 - 44.9    | 41.95 - 44.95    | 2           |

It is evident that the third class is the modal class. The mode lies somewhere between 35.95 and 38.95.

$$f_m = 14$$

$$f_1 = 4$$

$$f_2 = 8$$

$$\hat X = 35.95 + \frac{14 - 4}{(14 - 4) + (14 - 8)} \times 3$$

$$= 37.825$$

###### Histogram

![[Pasted image 20241105201828.png]]

###### Polygon Frequency

![[Pasted image 20241105201902.png]]

$$\hat X = 37.825$$