# Hitrecord

## `#!cpp void set_face_normal(const ray&, const vec3&)`

Imagine a `surface` $S$.  
If the `dot product`[^1] of incident `ray`[^2] and the `normal vector`[^1] is negative, the `ray`[^2] is outside of the `surface` $S$.  
![[surface_normals.svg]]

If our condition is `true` then the `normal` is the `outward normal`, otherwise it is opposite to `outward normal`.

```cpp
void hit_record::set_face_normal(const ray& r, const vec3& outward_normal) {
    // Sets the hit record normal vector.
    // NOTE: the parameter `outward_normal` is assumed to have unit length.

    front_face = dot(r.direction(), outward_normal) < 0;
    normal = front_face ? outward_normal : -outward_normal;
}
```

# References

[^1]: Read more about [[10. Introduction to vectors|dot product]].
[^2]: Read more about [[notes_publisher/docs/Projects/rayTracing/proj_raytracing_ray|ray]] in context of this project.