# Dielectric

## Members

### `#!cpp double refraction_index`

The `refractive index` $\eta$ of each dielectric material type.

## Methods

### Constructor

#### `#!cpp dielectric(double)`

Initializes `refractive index`.

```cpp
dielectric(double refraction_index) :
	refraction_index(refraction_index)
{}
```

### Normal

#### `#!cpp bool scatter(const ray&, const hit_record, color&, ray&)`

The `refractive index` of outside medium is $\eta^\prime$ and inside one is $\eta$.  
In the `main()`, the index is passed as  

$$\frac {\eta^\prime}{\eta}$$

Therefore, if the `ray`[^1] is coming from outside, `ri` is  

$$\frac \eta {\eta^\prime} = \frac 1 {\frac {\eta^\prime} \eta}$$

```cpp
double ri = rec.front_face ? (1.0 / refraction_index) : refraction_index;
```

Then for `unit vector`,[^2] we have

```cpp
vec3 unit_direction = unit_vector(r_in.direction());
```

From the `refract()` in [[Utils|utils]], we know that

```cpp
double cos_theta = std::fmin(dot(-unit_direction, rec.normal), 1.0);
```

Now using the identity  

$$\sin^2(\theta) + \cos^2(\theta) = 1$$

$$\implies \sin(\theta) = \sqrt{1 - \cos^2(\theta)}$$

```cpp
double sin_theta = std::sqrt(1.0 - cos_theta*cos_theta);
```

Light cannot `refract` if  

$$\frac {\eta}{\eta^\prime} \cdot \sin(\theta) > 1$$

In that case, we _reflect_ the light.  
For reflection, we can also use `Schlick's approximation`.

```cpp
if (cannot_refract || reflectance(cos_theta, ri) > random_double())
	direction = reflect(unit_direction, rec.normal);
else
	direction = refract(unit_direction, rec.normal, ri);
```

Therefore, we have

```cpp
bool scatter(const ray& r_in, const hit_record& rec, color& attenuation, ray& scattered) const override {
	attenuation = color(1.0, 1.0, 1.0);
	double ri = rec.front_face ? (1.0/refraction_index) : refraction_index;

	vec3 unit_direction = unit_vector(r_in.direction());

	double cos_theta = std::fmin(dot(-unit_direction, rec.normal), 1.0);
	double sin_theta = std::sqrt(1.0 - cos_theta*cos_theta);

	bool cannot_refract = ri * sin_theta > 1.0;
	vec3 direction;

	if (cannot_refract || reflectance(cos_theta, ri) > random_double())
		direction = reflect(unit_direction, rec.normal);
	else
		direction = refract(unit_direction, rec.normal, ri);

	scattered = ray(rec.p, direction);

	return true;
}
```

#### `#!cpp double reflectance(double, double)`

$$\left(\frac{1 - \eta}{1 + \eta}\right)^2 + \left(1 - \left(\frac{1 - \eta}{1 + \eta}\right)^2\right)(1 - \cos(\theta))^5$$

```cpp
static double reflectance(double cosine, double refraction_index) {
	// Use Schlick's approximation for reflectance.
	auto r0 = (1 - refraction_index) / (1 + refraction_index);
	r0 = r0*r0;
	return r0 + (1-r0)*std::pow((1 - cosine),5);
}
```

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in context of this project.
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].