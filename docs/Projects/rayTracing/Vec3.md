# Vec3

## Members

### `#!cpp double e[3];`

The values for each axis of a `vector`.[^1]  

1. $x$
2. $y$
3. $z$

## Methods

### Constructors

#### `#!cpp vec3()`

Default `constructor`, initializes the components to $0$.

```cpp
vec3::vec3() {
    e[0] = 0;
    e[1] = 0;
    e[2] = 0;
}
```

#### `#!cpp vec3(double e0, double e1, double e2)`

Takes the $x$, $y$ and $z$ components and sets them to:

1. `#!cpp e[0]`
2. `#!cpp e[1]`
3. `#!cpp e[2]`

```cpp
vec3::vec3(double e0, double e1, double e2) {
    e[0] = e0;
    e[1] = e1;
    e[2] = e2;
}
```

### Destructors

There is no `destructor` so far.

### Normal

#### `#!cpp double x()`

Returns the $x$ component.

```cpp
double vec3::x() const {
    return e[0];
}
```

#### `#!cpp double y()`

Returns the $y$ component.

```cpp
double vec3::y() const {
    return e[1];
}
```

#### `#!cpp double z()`

Returns the $z$ component.

```cpp
double vec3::z() const {
    return e[2];
}
```

#### `#!cpp double length()`

Returns `length` of the `vector`.[^1]

```cpp
double vec3::length() const {
    return std::sqrt(length_squared());
}
```

#### `#!cpp double length_squared()`

Returns the square of `length` of the `vector`.[^1]

```cpp
double vec3::length_squared() const {
    return e[0]*e[0] + e[1]*e[1] + e[2]*e[2];
}
```

### Operator Overloaded

#### `#!cpp operator-()`

Returns an `opposite vector`.[^1]

```cpp
vec3 vec3::operator-() const {
    return vec3(-e[0], -e[1], -e[2]); 
}
```

#### `#!cpp operator[](int i)`

Returns a component.

```cpp
double vec3::operator[](int i) const {
    return e[i]; 
}
```

#### `#!cpp operator+=(const vec3& v)`

Overwrites the `vector`[^1] by the `resultant vector`[^1] which results after the addition with $v$ `vector`.[^1]  
Then returns a `reference` to it.

```cpp
vec3& vec3::operator+=(const vec3& v) {
    e[0] += v.e[0];
    e[1] += v.e[1];
    e[2] += v.e[2];
    return *this;
}
```

#### `#!cpp operator*=(double t)`

Scales a `vector`[^1] _up_ by $t$ and returns a `reference` to it.

```cpp
vec3& vec3::operator*=(double t) {
    e[0] *= t;
    e[1] *= t;
    e[2] *= t;
    return *this;
}
```

#### `#!cpp operator/=(double t)`

Scales a `vector`[^1] _down_ by $t$ and returns a `reference` to it.

```cpp
vec3& vec3::operator/=(double t) {
    return *this *= 1/t;
}
```

### Static

#### `#!cpp vec3 random()`

Returns a random `vector`[^1] with magnitude ranging between

$$[0, 1)$$

```cpp
static vec3 random() {
	return vec3(random_double(), random_double(), random_double());
}
```

#### `#!cpp vec3 random(double min, double max)`

Returns a random `vector`[^1] with magnitude ranging between `min` and `max`.

```cpp
static vec3 random(double min, double max) {
	return vec3(random_double(min,max), random_double(min,max), random_double(min,max));
}
```

# References

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].