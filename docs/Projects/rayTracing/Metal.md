# Metal

## Members

### `#!cpp color albedo`

The whiteness of the material.

### `#!cpp double fuzz`

The amount of `fuzziness` we have in each reflection.

## Methods

### Constructor

#### `#!cpp metal(const color&, double)`

```cpp
metal(const color& albedo) :
	albedo(albedo),
	fuzz(fuzz < 1 ? fuzz : 1)
{}
```

### Normal

#### `#!cpp bool scatter(const ray&, const hit_record&, color&, ray&)`

Get a perfect reflected `ray`[^1] direction.

```cpp
vec3 reflected = reflect(r_in.direction(), rec.normal);
```

Add `fuzz` to it.  
![[fuzz.svg]]  
Get a random `unit vector`[^2] $\hat r$, scale it by `fuzz`.

```cpp
fuzz * random_unit_vector()
```

Then add it to the `unit vector`[^2] of the reflected `ray` .[^1] 

```cpp
reflected = unit_vector(reflected) + (fuzz * random_unit_vector());
```

Then make a `ray`[^1] out of it

```cpp
scattered = ray(rec.p, reflected);
```

To make sure that the `scattered ray`[^1] is projected outside of the surface after hitting it, we check if the `dot product`[^2] is positive.  
![[fuzz_correction.svg]]

```cpp
return (dot(scattered.direction(), rec.normal) > 0);
```

```cpp
bool scatter(const ray& r_in, const hit_record& rec, color& attenuation, ray& scattered) const override {
	vec3 reflected = reflect(r_in.direction(), rec.normal);
	reflected = unit_vector(reflected) + (fuzz * random_unit_vector());
	scattered = ray(rec.p, reflected);
	attenuation = albedo;
	return (dot(scattered.direction(), rec.normal) > 0);
}
```

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in the context of this project.
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].