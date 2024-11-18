# Metal

## Members

### `#!cpp color albedo`

The whiteness of the material.

## Methods

### `#!cpp bool scatter(const ray&, const hit_record&, color&, ray&)`

Get a perfect reflected `ray`[^1] direction.

```cpp
vec3 reflected = reflect(r_in.direction(), rec.normal);
```

Then make a `ray`[^1] out of it

```cpp
scattered = ray(rec.p, reflected);
```

```cpp
bool scatter(const ray& r_in, const hit_record& rec, color& attenuation, ray& scattered) const override {
	vec3 reflected = reflect(r_in.direction(), rec.normal);
	scattered = ray(rec.p, reflected);
	attenuation = albedo;
	return true;
}
```

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in the context of this project.