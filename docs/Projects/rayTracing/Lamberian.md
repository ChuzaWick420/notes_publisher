# Lamberian

## Members

### `#!cpp color albedo`

The whiteness of a material.

## Methods

### Constructors

#### `#!cpp lambertian(const color& albedo)`

Initializes the `albedo`.

```cpp
lambertian(const color& albedo) : albedo(albedo) {}
```

### Normal

#### `#!cpp bool scatter(const ray&, const hit_record&, color&, ray&)`

Determine a random direction for the reflected ray

```cpp
auto scatter_direction = rec.normal + random_unit_vector();
```

then make that `ray`[^1] 

```cpp
scattered = ray(rec.p, scatter_direction);
```

```cpp
bool scatter(const ray& r_in, const hit_record& rec, color& attenuation, ray& scattered) const override {
	auto scatter_direction = rec.normal + random_unit_vector();
	scattered = ray(rec.p, scatter_direction);
	attenuation = albedo;
	return true;
}
```

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in the context of this project.