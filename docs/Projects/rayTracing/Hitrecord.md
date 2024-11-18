# Hitrecord

## Members

### `#!cpp point3 p`

A 3D point where `ray`[^1] hits the `surface` of an object.

### `#!cpp vec3 normal`

The `normal` to the `surface`.

### `#!cpp double t`

The distance between eye and `ray`[^2] hitting the object.

### `#!cpp bool front_face`

Checking if the `ray`[^2] hit from outside or inside of the object.

## Methods

### Constructors

This class has no `constructors`.

### Destructors

This class has no `destructors`.

### Normal

#### `#!cpp void set_face_normal(const ray&, const vec3&)`

Imagine a `surface` $S$.  
If the `dot product`[^2] of incident `ray`[^1] and the `normal vector`[^2] is negative, the `ray`[^1] is outside of the `surface` $S$.  
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

### Operator Overloaded

There are no overloaded methods.

### Static

There are no static methods.

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in context of this project.
[^2]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|dot product]].