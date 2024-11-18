# Interval

## Members

### Normal

#### `#!cpp double min`

The lower bound of the `interval`.[^1]  

#### `#!cpp double max`

The upper bound of the `interval`.[^1]

### Static

#### `#!cpp const interval empty`

$$(\infty, -\infty)$$

#### `#!cpp const interval universe`

$$(-\infty, \infty)$$

## Method

### Constructors

Takes the `min` and `max` values and sets the boundaries.

```cpp
interval(double min, double max) : min(min), max(max) {}
```

### Normal

#### `#!cpp double size()`

Returns the gap between `min` and `max`.

```cpp
double interval::size() const {
    return max - min;
}
```

#### `#!cpp bool contains(double)`

Checks if the `interval`[^1] contains a point or not, point can exist on boundaries.

```cpp
bool interval::contains(double x) const {
    return min <= x && x <= max;
}
```

#### `#!cpp bool surrounds(double)`

Checks if the `interval`[^1] contains a point or not, point cannot exist on boundaries.

```cpp
bool interval::surrounds(double x) const {
    return min < x && x < max;
}
```

#### `#!cpp Double clamp(double x)`

```cpp
double interval::clamp(double x) const {
    if (x < min)
        return min;
    if (x > max)
        return max;
    return x;
}
```

## References

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].