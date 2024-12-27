# Utils

## `#!cpp random_on_hemisphere`

![[hemisphere_creation.svg]]  
We first generate a random `unit vector`.[^1]  

```cpp
vec3 on_unit_sphere = random_unit_vector();
```

Using the `normal vector`,[^1] we just see if the `dot product`[^1] is positive or not.  
If it it positive, then this is the vector on correct `hemisphere`, otherwise it is on the wrong one.

```cpp
if (dot(on_unit_sphere, normal) > 0.0)
	return on_unit_sphere;
else
	return -on_unit_sphere;
```

Full `function`.[^2]

```cpp
inline vec3 random_on_hemisphere(const vec3& normal) {
    vec3 on_unit_sphere = random_unit_vector();
    if (dot(on_unit_sphere, normal) > 0.0) // In the same hemisphere as the normal
        return on_unit_sphere;
    else
        return -on_unit_sphere;
}
```

## `#!cpp vec3 reflect(const vec3&, const vec&)`

![[reflection.svg]]

```cpp
inline vec3 reflect(const vec3& v, const vec3& n) {
    double d_mag = dot(v, unit_vector(n));
    vec3 d = unit_vector(n) * d_mag;
    vec3 b = -d;
    return v + 2 * b;
}
```

## `#!cpp vec3 refract(const vec3&,const vec3&, double)`

According to `snell's law`  

$$\eta \cdot \sin(\theta) = \eta^\prime\cdot\sin(\theta^\prime)$$

Where $\theta$ and $\theta^\prime$ are angles of incident `ray`[^3] and refracted `ray`[^3] against the `normal vector`.[^1]  
And $\eta$ and $\eta^\prime$ are refractive indices of incident `ray`[^3] and refracted `ray`.[^3]  
If $R^\prime$ is the refracted `ray`[^3] then we can break it into components which are parallel or perpendicular to the `normal vector`.[^1]  

$$\vec R^\prime = \vec R^\prime_\parallel + \vec R^\prime_\perp$$

![[refraction.svg]]  

$$\vec R_\perp = \vec {R^\prime_x} = \frac \eta {\eta^\prime} \sin(\theta) \hat{R_x}$$

$$\because \sin(\theta) \hat{R_x} = \vec{R_x}$$

$$= \frac \eta {\eta^\prime} \vec {R_x}$$

Also notice  

$$\vec {R_x} = \vec R + \cos(\theta) \cdot \vec n$$

From the `dot product`[^1]  

$$- \vec R \cdot \vec n = Rn \cos(\theta)$$

Since our $\vec R$ and $\vec n$ are `unit vectors`.[^1]  

$$- \vec R \cdot \vec n = \cos(\theta)$$

Therefore,  

$$\vec {R_\perp} = \frac \eta {\eta^\prime}(\vec R + (- \vec R \cdot \vec n)\vec n)$$

To find $- \vec R \cdot \vec n$, we have

```cpp
auto cos_theta = std::fmin(dot(-uv, n), 1.0);
```

And to solve rest, we have

```cpp
vec3 r_out_perp =  etai_over_etat * (uv + cos_theta*n);
```

Now for $\vec R_\parallel$ we can use `Pythagorus theorem`.  

$$(R^\prime)^2 = (R^\prime_\perp)^2 + (R^\prime_\parallel)^2$$

$$\implies 1 - (R^\prime_\perp)^2 = (R^\prime_\parallel)^2$$

$$R^\prime_\parallel = \sqrt{1 - R^\prime_\perp}$$

and for the direction, we have $- \vec n$.  

$$\therefore \vec R_\parallel = - \vec n \sqrt{1 - R^\prime_\perp}$$

This is given by

```cpp
vec3 r_out_parallel = -std::sqrt(std::fabs(1.0 - r_out_perp.length_squared())) * n;
```

Hence we have

```cpp
inline vec3 refract(const vec3& uv, const vec3& n, double etai_over_etat) {
    auto cos_theta = std::fmin(dot(-uv, n), 1.0);
    vec3 r_out_perp =  etai_over_etat * (uv + cos_theta*n);
	vec3 r_out_parallel = -std::sqrt(std::fabs(1.0 - r_out_perp.length_squared())) * n;
    return r_out_perp + r_out_parallel;
}
```

## References

[^1]: Read more about [[10. Introduction to vectors|vectors]].
[^2]: Read more about [[M_Function|functions]].
[^3]: Read more about [[notes_publisher/docs/Projects/rayTracing/proj_raytracing_ray|ray]] in context of this project.