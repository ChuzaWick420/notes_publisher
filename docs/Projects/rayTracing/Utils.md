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

## References

[^1]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
[^2]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].