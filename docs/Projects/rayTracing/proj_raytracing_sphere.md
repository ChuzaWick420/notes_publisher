# Sphere

![[Proj_raytracing_sphere_definition.svg]]  

$$\vec P + \vec r = \vec C$$

$$\implies \vec r = \vec C - \vec P$$

We know that for a `sphere`, we have

$$(C_x - x)^2 + (C_y - y)^2 + (C_z - z)^2 = r^2$$

where $\vec C$ is the `position vector`[^1] for the `center` and $\vec P$ is the `position vector`[^1] where a `ray`[^2] hits the `sphere`.

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

$$t = \frac{h \pm \sqrt{h^2 - 4ac}}{a}$$

We can use `discriminant` to find the nature of the roots,  
![[Proj_raytracing_sphere_roots.svg]]  
Let $D$ be `discriminant` such that  

$$D = h^2 - 4ac$$

then  
For no hit  

$$D < 0$$

For one hit  

$$D = 0$$

For two hits  

$$D > 0$$

## `#!cpp bool hit()`

This `function` depends a lot on the `discriminant` and `quadratic formula`, first we show the relation between the mathematical terms and the code terms.

- $\vec A$ is `#!cpp r.origin()`
- $\vec b$ is `#!cpp r.direction()`
- $\vec C$ is `#!cpp center`
- $\vec C - \vec A$ is therefore, `#!cpp center - r.origin()`
- $h = \vec b \cdot (\vec C - \vec A)$ is `#!cpp dot(r.origin(), oc)`
- $c = (\vec C - \vec A) \cdot (\vec C - \vec A) - r^2$ is `#!cpp oc.length_squared() - radius * radius`

> [!NOTE]- Explanation for $c$  
> 
> $$\vec {oc} = x \hat i + y \hat j$$
> 
> $$\implies \vec {oc} \cdot \vec {oc} = x^2 + y^2$$
> 
> $$= \left(\sqrt{x^2 + y^2}\right)^2$$
> 
> $$= (\text{len}(\vec {oc}))^2$$

The `discriminant`

```cpp
vec3 oc = center - r.origin();
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

![[Proj_raytracing_sphere_roots_2.svg]]

```cpp
auto sqrtd = std::sqrt(discriminant);

// Find the nearest root that lies in the acceptable range.
auto root = (h - sqrtd) / a;
```

Then we are checking if both of the `roots` are within the acceptable `interval`[^3] or not.  
![[Proj_raytracing_interval.svg]]

```cpp
if (!ray_t.surrounds(root)){
    root = (h + sqrtd) / a;

    if (!ray_t.surrounds(root))
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
    if (!ray_t.surrounds(root)){
        root = (h + sqrtd) / a;
 
        if (!ray_t.surrounds(root))
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

[^1]: Read more about [[10. Introduction to vectors|vectors]].
[^2]: Read more about the [[notes_publisher/docs/Projects/rayTracing/proj_raytracing_ray|proj_raytracing_ray]] in context of this project.
[^3]: Read more about [[mth101_01|intervals]].