# Sphere

![[sphere_definition.svg]]  

$$\vec P + \vec r = \vec C$$

$$\implies \vec r = \vec C - \vec P$$

We know that for a `sphere`, we have

$$(C_x - x)^2 + (C_y - y)^2 + (C_z - z)^2 = r^2$$

where  

$$\vec C = <C_x, C_y, C_z>$$

$$\vec P = <x, y, z>$$

Using `dot product`[^1]

$$(C_x - x)^2 + (C_y - y)^2 + (C_z - z)^2 = (\vec C - \vec P) \cdot (\vec C - \vec P)$$

$$\implies  (\vec C - \vec P) \cdot (\vec C - \vec P) = r^2$$

Putting the parametric equation for `ray`[^2]  

$$(\vec C - (\vec A + t \vec b)) \cdot (\vec C - (\vec A + t \vec b)) = r^2$$

If we try to open it up, we get  

$$t^2 \vec b \cdot \vec b - 2t \vec b \cdot (\vec C - \vec A) + (\vec C - \vec A) \cdot (\vec C - \vec A) = r^2$$

We are trying to solve for $t$ here.  

$$a = \vec b \cdot \vec b$$

$$b = -2 \vec b \cdot (\vec C - \vec A)$$

$$c = (\vec C - \vec A) \cdot (\vec C - \vec A) - r^2$$

Notice how $b$ has a factor of $-2h$.  
Where  

$$h = \vec b \cdot (\vec C - \vec A)$$

Using the `quadratic equation`.  

$$\frac {-b \pm \sqrt{b^2 - 4ac}}{2a}$$

$$= \frac {-(-2h) \pm \sqrt{(-2h)^2 - 4ac}}{2a}$$

$$= \frac{2h \pm 2\sqrt{h^2 - 4ac}}{2a}$$

$$= \frac{h \pm \sqrt{h^2 - 4ac}}{2a}$$

We can use `discriminant` to find the nature of the roots,  
![[sphere_roots.svg]]  
Let $D$ be `discriminant` such that  

$$D = h^2 - 4ac$$

then  
For no hit  

$$D < 0$$

For one hit  

$$D = 0$$

For two hits  

$$D > 0$$

## Members

### `#!cpp point3 center`

The `center` of the `sphere`.

### `#!cpp double radius`

The `radius` of the `sphere`.

## Methods

### `#!cpp hit()`

The center from the point of intersection between the `sphere` surface and the `ray`.[^2]

```cpp
vec3 oc = center - r.origin();
```

The `discriminant`

```cpp
auto a = r.direction().length_squared();
auto h = dot(r.direction(), oc);
auto c = oc.length_squared() - radius*radius;

auto discriminant = h*h - a*c;
```

Skipping processing if the `ray`[^2] does not even hits the `sphere`. i.e. the roots are `imaginary`.

```cpp
if (discriminant < 0)
	return false;
```

We know that `roots` are going to be  

$$t = \frac{h \pm \sqrt D}{a}$$

$$\implies t = \frac{h}{a} \pm \frac{\sqrt D}{a}$$

![[sphere_roots_2.svg]]

```cpp
auto sqrtd = std::sqrt(discriminant);

// Find the nearest root that lies in the acceptable range.
auto root = (h - sqrtd) / a;
```

Then we are checking if both of the `roots` are within the acceptable `interval`[^3] or not.  
![[interval.svg]]

```cpp
if (root <= ray_t.min || ray_t.max <= root) {
	root = (h + sqrtd) / a;
	if (root <= ray_t.min || ray_t.max <= root)
		return false;
}
```

If both `roots` are not in the `interval`,[^3] we are skipping these `roots`.

```cpp
rec.t = root;
rec.p = r.at(rec.t);
rec.normal = (rec.p - center) / radius;

vec3 outward_normal = (rec.p - center) / radius;
rec.set_face_normal(r, outward_normal);
```

```cpp
bool sphere::hit(const ray& r, interval ray_t, hit_record& rec) const override {
	vec3 oc = center - r.origin();
	auto a = r.direction().length_squared();
	auto h = dot(r.direction(), oc);
	auto c = oc.length_squared() - radius*radius;

	auto discriminant = h*h - a*c;
	if (discriminant < 0)
		return false;

	auto sqrtd = std::sqrt(discriminant);

	// Find the nearest root that lies in the acceptable range.
	auto root = (h - sqrtd) / a;
	if (root <= ray_t.min || ray_t.max <= root) {
		root = (h + sqrtd) / a;
		if (root <= ray_t.min || ray_t.max <= root)
			return false;
	}

	rec.t = root;
	rec.p = r.at(rec.t);
	rec.normal = (rec.p - center) / radius;

	vec3 outward_normal = (rec.p - center) / radius;
	rec.set_face_normal(r, outward_normal);

	return true;
}
```

## References

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
[^2]: Read more about the [[notes_publisher/docs/Projects/rayTracing/Ray|Ray]] in context of this project.
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].