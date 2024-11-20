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

### `#!cpp std::shared_ptr<material> mat`

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
Otherwise, we record how far did the `ray`[^2] hit the `sphere`.

```cpp
rec.t = root;
```

Then also record _where_ did the `ray`[^2] hit in space.

```cpp
rec.p = r.at(rec.t);
```

Then the surface `normal` will be

$$\vec n = \vec P - \vec C$$

Where $\vec P$ is where the `ray`[^2] hit,  
being the head of `resultant vector`[^1] and $\vec C$ being a `position vector`[^1] for `center`, being the tail of `resultant vector`.[^1]

```cpp
rec.normal = (rec.p - center);
```

To convert it to a `unit vector`,[^1] we will divide by the `radius` of the `sphere`.

```cpp
rec.normal = (rec.p - center) / radius;
```

Set the `normal` to always face towards the `camera`.

```cpp
vec3 outward_normal = rec.normal;
rec.set_face_normal(r, outward_normal);
```

Hence the full code becomes

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
	vec3 outward_normal = rec.normal;
	rec.set_face_normal(r, outward_normal);

	rect.mat = mat;

	return true;
}
```

## References

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
[^2]: Read more about the [[notes_publisher/docs/Projects/rayTracing/Ray|Ray]] in context of this project.
[^3]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].