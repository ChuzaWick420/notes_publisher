---
tags:
  - university-notes
university-name: 
date: 2024-11-05
---

<span style="color: gray;">Dated: 05-11-2024</span>

# Lecture No. 4

## Example

The Environmental Protection Agency tests all new car models for mileage ratings, obtaining 30 measurements for a specific new model.

| 36.3 | 42.1 | 44.9 |
| ---- | ---- | ---- |
| 30.1 | 37.5 | 32.9 |
| 40.5 | 40.0 | 40.2 |
| 36.2 | 35.6 | 35.9 |
| 38.5 | 38.8 | 38.6 |
| 36.3 | 38.4 | 40.5 |
| 41.0 | 39.0 | 37.0 |
| 37.0 | 36.7 | 37.1 |
| 37.1 | 34.8 | 33.9 |
| 39.9 | 38.1 | 39.8 |

### Construction of a Frequency Distribution

#### Step 1

Identify the smallest and the largest measurements in the data set.  

$$\text {Smallest Value} = X_0 = 30.1$$

$$\text {Largest Value} = X_m = 44.9$$

#### Step 2

Find the range which is defined as the difference between the largest value and the smallest value.

$$\text{Range} = X_m - X_0$$

$$= 44.9 – 30.1$$

$$= 14.8$$

#### Step 3

Decide on the number of classes for grouping the data.  
Typically, large datasets use 10-20 classes.  
For this 30-observation dataset, we choose 5 classes.

#### Step 4

$$\text{Class Interval} = h = \frac{14.8}{5} = 2.96 = 3$$

This means that our big interval will be divided into small sub-intervals, each of which will be 3 units long.

#### Step 5

Start the lowest class from a number equal to or slightly less than the smallest data value.  
Here, with 30.1 as the smallest value, we set the lower class limit at 30.0.

#### Step 6

Determine the lower class limits of the successive classes by adding $h = 3$ successively.

| Class Number | Lower Class Limit |
| ------------ | ----------------- |
| 1            | 30.0              |
| 2            | 30.0 + 3 = 33.0   |
| 3            | 33.0 + 3 = 36.0   |
| 4            | 36.0 + 3 = 39.0   |
| 5            | 39.0 + 3 = 42.0   |

#### Step 7

Set upper class limits to cover the largest data value, with each limit differing by $h$. These limits are shown in the table's third column.

| Class Number | Lower Class Limit | Upper Class Limit |
| ------------ | ----------------- | ----------------- |
| 1            | 30.0              | 32.9              |
| 2            | 30.0 + 3 = 33.0   | 32.9 + 3 = 35.9   |
| 3            | 33.0 + 3 = 36.0   | 35.9 + 3 = 38.9   |
| 4            | 36.0 + 3 = 39.0   | 38.9 + 3 = 41.9   |
| 5            | 39.0 + 3 = 42.0   | 41.9 + 3 = 44.9   |

Hence we obtain the following classes

| Classes     |
| ----------- |
| 30.0 - 32.9 |
| 33.0 - 35.9 |
| 36.0 - 38.9 |
| 39.0 - 41.9 |
| 42.0 - 44.9 |

We use 30.0 to 32.9 instead of 30 to 33 to avoid ambiguity when classifying data.  
If 33 were included in both classes, it would create confusion about its placement.  
Thus, the class interval remains 3, not 2.9, a point clarified later with the concept of class boundaries.

#### Step 8

After forming the classes, distribute the data into the appropriate classes and find the frequency of each class.

|   Classes   | Frequency |
| :---------: | :-------: |
| 30.0 - 32.9 |     2     |
| 33.0 - 35.9 |     4     |
| 36.0 - 38.9 |    14     |
| 39.0 - 41.9 |     8     |
| 42.0 - 44.9 |     2     |
|             |    30     |

### Class Boundaries

The true class limits of a class are known as its `class boundaries`.

| Class Limit | Class Boundaries | Frequency |
| :---------: | :--------------: | :-------: |
| 30.0 - 32.9 |  29.95 - 32.95   |     2     |
| 33.0 - 35.9 |  32.95 - 35.95   |     4     |
| 36.0 - 38.9 |  35.95 - 38.95   |    14     |
| 39.0 - 41.9 |  38.95 - 41.95   |     8     |
| 42.0 - 44.9 |  41.95 - 44.95   |     2     |
|             |      Total       |    30     |

The difference between the upper and lower class boundaries of any class is equal to the class interval $h=3$.  
For instance, $32.95−29.95=3$ and $35.95−32.95=3$.  
Class boundaries should extend to one decimal place beyond the data to prevent observations from falling exactly on the boundary, ensuring they are classified correctly.  
We also explore relative frequency and percentage frequency distributions: relative frequency is found by dividing each frequency by the total observations, while percentage frequency is obtained by multiplying relative frequency by $100$.

| Class Limit | Frequency | Relative Frequency | %age Frequency |
| ----------- | --------- | ------------------ | -------------- |
| 30.0 - 32.9 | 2         | 2/30 = 0.067       | 6.7            |
| 33.0 - 35.9 | 4         | 4/30 = 0.133       | 13.3           |
| 36.0 - 38.9 | 14        | 14/30 = 0.467      | 4.67           |
| 39.0 - 41.9 | 8         | 8/30 = 0.267       | 26.7           |
| 42.0 - 44.9 | 2         | 2/30 = 0.067       | 6.7            |
|             | 30        |                    |                |

‘Relative frequencies’ refers to the frequencies of different classes in relation to the total number of observations.  
Creating a relative frequency distribution allows for comparison between two datasets with similar classes.  
For instance, the Environmental Protection Agency may test two car models, A and B, and present their frequency distributions for comparison.

| MILEAGE     | FREQUENCY |     |
| ----------- | --------- | --- |
|             | A         | B   |
| 30.0 - 32.9 | 2         | 7   |
| 33.0 - 35.9 | 4         | 10  |
| 36.0 - 38.9 | 14        | 16  |
| 39.0 - 41.9 | 8         | 9   |
| 42.0 - 44.9 | 2         | 8   |
|             | 30        | 50  |

In order to be able to compare the performance of the two car models, we construct the relative frequency distributions in the percentage form:

| MILEAGE     | Model A            | Model B          |
| ----------- | ------------------ | ---------------- |
| 30.0 - 32.9 | 2/30 x 100 = 6.7   | 7/50 x 100 = 14  |
| 33.0 - 35.9 | 4/30 x 100 = 13.3  | 10/50 x 100 = 20 |
| 36.0 - 38.9 | 14/30 x 100 = 46.7 | 16/50 x 100 = 32 |
| 39.0 - 41.9 | 8/30 x 100 = 26.7  | 9/50 x 100 = 18  |
| 42.0 - 44.9 | 2/30 x 100 = 6.7   | 8/50 x 100 = 16  |

The table indicates that 6.7% of model A cars fall within the mileage range of 42.0 to 44.9, compared to 16% for model B, allowing for various comparisons.  
Next, we'll explore the visual representation of continuous frequency distributions, focusing on histograms, frequency polygons, and frequency curves.

### Histograms

A histogram is made up of adjacent rectangles where the bases represent class boundaries on the X-axis and the heights correspond to the frequencies of each class.  
Previously, we discussed the mileage ratings of cars inspected by the Environmental Protection Agency, resulting in the following frequency table:

| Class Limit | Class Boundaries | Frequency |
| ----------- | ---------------- | --------- |
| 30.0 - 32.9 | 29.95 - 32.95    | 2         |
| 33.0 - 35.9 | 32.95 - 35.95    | 4         |
| 36.0 - 38.9 | 35.95 - 38.95    | 14        |
| 39.0 - 41.9 | 38.95 - 41.95    | 8         |
| 42.0 - 44.9 | 41.95 - 44.95    | 2         |
|             | Total            | 30        |

![[Pasted image 20241105155012.png]]

### Frequency Polygons

A `frequency polygon` is obtained by plotting the class frequencies against the mid-points of the classes, and connecting the points so obtained by straight line segments.

| Class Boundaries | Mid-Point (X) | Frequency (f) |
| ---------------- | ------------- | ------------- |
| 26.95 - 29.95    | 28.45         | 0             |
| 29.95 - 32.95    | 31.45         | 2             |
| 32.95 - 35.95    | 34.45         | 4             |
| 35.95 - 38.95    | 37.45         | 14            |
| 38.95 - 41.95    | 40.45         | 8             |
| 41.95 - 44.95    | 43.45         | 2             |
| 44.95 - 47.95    | 46.45         | 0             |

Next, we plot points on our graph paper according to the frequencies of the various classes, and join the points so obtained by straight line segments.

![[Pasted image 20241105162109.png]]

A `polygon` is defined as a many-sided closed figure, and we want our frequency polygon to be closed.  
To achieve this, we added two classes with zero frequency to our table.  
This allows the line segment to touch the X-axis at both ends, forming a closed figure.

### Frequency Curves

This is the _smoothed_ version of the [frequency polygon](#frequency-polygons).  
![[Pasted image 20241105162741.png]]