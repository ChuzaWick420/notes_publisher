# Main

## Class Diagram

```mermaid
classDiagram

class Vec3 {
+ axes : Array[int, 3]
+ Vec3() void
+ Vec3(double, double, double) void
+ x() double
+ y() double
+ z() double
+ length() double
+ length_squared() double
+ is_near_zero() bool
+ static random() Vec3
+ static random(double, double) Vec3
+ operator-() Vec3
+ operator[](int) double
+ operator+=(Vec3&) Vec3&
+ operator*=(double) Vec3&
+ operator/=(double) Vec3&
}

class Material {
+ virtual ~Material() void
+ virtual scatter(Ray&, Hit_record&, Color&, Ray&) bool
}

class Ray {
+ Ray() void
+ Ray(Point&, Vec3&) void
+ origin() Point3&
+ direction() Vec3&
+ at(double) Point3
- orig : Point3
- dir : Vec3
}

class Interval {
+ min : double
+ max : double
+ empty : Interval
+ universe : Interval
+ Interval() void
+ Interval(double, double) void
+ size() double
+ contains(double) bool
+ surrounds(double) bool
+ clamp(double) double
}

class Sphere {
- center : Point3
- radius : double
- mat shared_ptr<Material>
+ Sphere(Point3&, double, shared_ptr<Material>) void
+ hit(Ray&, Interval, Hit_record&) bool
}

class Lambertian {
+ Lambertian(Color&) void
+ scatter(Ray&, Hit_record&, Color&, Ray&) bool
- albedo : Color
}

class Dielectric {
+ Dielectric(double) void
+ scatter(Ray&, Hit_record&, Color&, Ray&) bool
- refractive_index : double
- static reflectance(double, double) double
}

class Metal {
+ Metal(Color&, double) void
+ scatter(Ray&, Hit_record&, Color&, Ray&) bool
- albedo : Color
- fuzz : double
}

class Hittable {
+ virtual ~Hittable() void
+ virtual hit(Ray&, Interval, Hit_record&) bool
}

class Hittable_list {
+ objects : vector<shared_ptr<Hittable>>
+ Hittable_list() void
+ Hittable_list(shared_ptr<Hittable>) void
+ clear() void
+ add(shared_ptr<Hittable>) void
+ hit(Ray&, Interval, Hit_record&) bool
}

class Hit_record {
+ p : Point3
+ normal : Vec3
+ t : double
+ front_face : bool
+ mat : shared_ptr<Material>
+ set_face_normal(Ray&, Vec3&) void
}

class Camera {
+ aspect_ratio : double
+ img_width : int 
+ samples_per_pixel : int 
+ max_depth : int 
+ img_gen : bool 
+ vfov : double 
+ lookfrom : Point3 
+ lookat : Point3 
+ vup : Vec3 
+ threads : int 
+ defocus_angle : double 
+ focus_dist : double 
+ render(Hittable&) void
+ ~Camera() void
- pixel_grid : vector<Color> 
- worker_threads : vector<thread> 
- window_width : int 
- img_height : int 
- center : Point3 
- pixel00_loc : Point3 
- pixel_delta_u : Vec3 
- pixel_delta_v : Vec3 
- pixel_samples_scale : double 
- u : Vec3 
- v : Vec3 
- w : Vec3 
- i_image : Image 
- defocus_disk_u : Vec3 
- defocus_disk_v : Vec3 
- show_img() void
- initialize() void
- defocus_disk_sample() Point3
- sample_square() Vec3
- get_ray(int, int) Ray
- ray_color(Ray&, int, Hittable&) Color
}

Material <|-- Lambertian
Material <|-- Dielectric
Material <|-- Metal

Hittable <|-- Hittable_list
```

Our first task is to have a way to display whatever the heck we are trying to display.  
For that, I am using [SFML](https://github.com/SFML/SFML).


A `ray tracer` is responsible for following tasks.

1. Shooting rays out of the eye.
2. Determining which objects are being hit by that ray at closest.
3. Determine the color of pixel to show on screen.

Now we need to know what a `ray`[^1] is.  
Checkout `aspect ratio` variable in [[Camera|camera]].  
Using this, we will determine dimensions of the following

1. `Image`
2. `Viewport` (a virtual 2D rectangle in the space which shows the image)
3. `Window`

Selecting an arbitrary `height` _or_ `width` for any of these, we can find the other.  

$$\frac {\text{width}}{\text{height}} = \text{aspect ratio}$$

To start off, we will try drawing a _sky_ which is going to be just a gradient from `blue` to `white`.  
For that, we will use a `lerp function`.  
This will _smoothly_ transition from `blue` to `white`.

> [!NOTE] `blue` and `white` both are `colors`[^2] consisting of $r$, $g$ and $b$ values.  

Read about `camera::ray_color` in [[Camera|camera]].

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in context of this project.
[^2]: Read more about [[Vec3|colors]].