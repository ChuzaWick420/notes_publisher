# Camera

## `#!cpp void initialize()`

The `f_focal_length` variable controls the distance of `camera` from the object of focus.  
![[Proj_raytracing_focal_length.svg]]  
Here $f$ is the `focal_length`.  
We control the `aspect ratio` and `image_width` manually.

The value of `focal_length` and dimensions of `viewport` don't hold much value as long as they are both scaled equally.  
In the following figure, $\frac {V_h} 2$ is the `viewport_height` and $S$ is any random `scalar` value.  
![[Proj_raytracing_viewport_dimensions.svg]]

The following variables `#!cpp u_pixel_delta_u` and `#!cpp u_pixel_delta_v` are represented in the following figure, represented by  

$$\vec {\Delta u}$$

$$\vec {\Delta v}$$

![[Proj_raytracing_viewport.svg]]

The `viewport_upper_left` is given by  
![[Proj_raytracing_viewport_upper_left.svg]]

Similarly, `pixel00_loc` is given by  
![[Proj_raytracing_pixel00_loc.svg]]

## `#!cpp void render(const hittable&)`

First, we call the `camera::initialize()`.

```cpp
initialize();
```

resize the grid

```cpp
pixel_grid.resize(img_height * img_width);
```

Then, we will iterate over our 1 dimensional `pixel_grid`.

```cpp
for (auto& pixel : pixel_grid) {}
```

We will also need keep track of each iteration using an `index`.

```cpp
int index = 1;
```

For the $x$ coordinate of each pixel, we do

```cpp
int x = (index - 1) % img_width;
```

![[Proj_raytracing_modulo.svg]]

in the figure above, the `image_width` is $3$.  
Similarly for $y$ coordinate, we do

```cpp
int y = (index - 1) / img_width;
```

then for anti-aliasing, we iterate over each sample and get the overall `color`.[^1]

```cpp
for (int sample = 0; sample < samples_per_pixel; sample++) {
	ray r = get_ray(x, y);
	pixel_color += ray_color(r, max_depth, world);
}
```

Then in the end, we write the color

```cpp
write_color(&pixel, pixel_color * pixel_samples_scale);
```

then we show the image

```cpp
this->show();
```

```cpp
void camera::render(const hittable& world) {
    initialize();

    pixel_grid.resize(img_height * img_width);

    int index = 1;

    for (auto& pixel : pixel_grid) {
        color pixel_color(0, 0, 0);

        int x = (index - 1) % img_width;
        int y = (index - 1) / img_width;

        for (int sample = 0; sample < samples_per_pixel; sample++) {
            ray r = get_ray(x, y);
            pixel_color += ray_color(r, max_depth, world);
        }

        write_color(&pixel, pixel_color * pixel_samples_scale);

        index++;
    }

   this->show_img();
}
```

## `#!cpp vec3 sample_square()`

Get's a random `vector`[^1] in a `square space` with dimensions  

$$1 \times 1$$

With `width` and `height` both ranging in $[-0.5, 0.5]$.

```cpp
vec3 camera::sample_square() const {
    return vec3(random_double() - 0.5, random_double() - 0.5, 0);
}
```

## `#!cpp ray get_ray(int, int)`

![[Proj_raytracing_sampling.svg]]  
We will need `pixel00_loc` are reference point.

```cpp
ray camera::get_ray(int u, int v) const {
    auto offset = sample_square();
    auto pixel_sample = pixel00_loc
                        + ((u + offset.x()) * pixel_delta_u)
                        + ((v + offset.y()) * pixel_delta_v);

    auto ray_origin = center;
    auto ray_direction = pixel_sample - ray_origin;

    return ray(ray_origin, ray_direction);
}
```

## `#!cpp color ray_color(const ray&, int, const hittable&)`

So our task is to smoothly transform each `color`[^1] component into the component of the other `color`,[^1] depending on some variable.  
For our purpose, we can use the $y$ component of the `ray`[^2] to play that role since it changes according to `height`.  
![[Proj_raytacing_interpolation.svg]]  
We need an equation for that `line`[^3]  

$$\frac {y_2 - y_1}{x_2 - x_1} = \frac{y - y_1}{x - x_1}$$

$$(y_2 - y_1) \cdot (x - x_1) = (y - y_1) \cdot (x_2 - x_1)$$

We know that $y_1$ and $y_2$ are the component values of `blue` and `white` respectively and let's label them as $B$ and $W$.  
Also, we want $x_1$ and $x_2$ to be $0$ and $1$ for simplicity.  
Then the equation becomes.  

$$(W - B) \cdot (h - 0) = (y(h) - B) \cdot (1 - 0)$$

$$(W - B)h = y(h) - B$$

$$y(h) = (W - B)h + B$$

$$y(h) = Wh - Bh + B$$

$$y(h) = Wh + B - Bh$$

$$y(h) = Wh + B(1 - h)$$

This `function`[^4] returns the pixel color for each `ray`[^2] for the _sky_.

```cpp
vec3 unit_direction = unit_vector(r.direction());
```

There is a slight problem though  
![[Proj_raytracing_unit _vec.svg]]  
The $y$ component of the `unit vector`[^5] is in $[-1, 1]$ so we need to modify some of our maths for it.  
![[Proj_raytracing_unit_vec_2.svg]]  
So the `interval`[^6] we are working with is $[-1, 1]$ and we want it to be $[0, 1]$  
First thing to realize is that if we add $1$ to our input, the `interval`[^6] becomes  

$$[-1, 1] \to [0, 2]$$

```cpp
unit_direction.y() + 1.0f;
```

then dividing by $2$, it is within $[0, 1]$  

$$[0, 2] \to [0, 1]$$

```cpp
auto a = 0.5*(unit_direction.y() + 1.0);
```

Let's take a look at our equation again

$$y(h) = Wh + B(1 - h)$$

The way we will be sending the `rays`[^3] is going to be opposite to the direction of $y$ component of `unit vector`.[^5]  
Since the direction is opposite, so the $W$ is replaced by $B$ and vise versa.

$$y(a) = (1 - h)W + hB$$

And this applies over all components of the `color`[^1]

```cpp
(1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0);
```

There can be multiple bounces, therefore, we will recursively call this `function`[^4] and limit the number of such bounces using a `depth` value.

```cpp
if (depth <= 0)
	return color(0, 0, 0);
```

We will look for collisions within  

$$[0.001, \infty)$$

```cpp
world.hit(r, interval(0.001, infinity), rec)
```

For each light bounce, we will calculate the scattered `ray`[^2] direction.  

```cpp
rec.mat->scatter(r, rec, attenuation, scattered)
```

Also, we will decrease the luminance by `attenuation` value.

```cpp
attenuation * ray_color(scattered), depth - 1, world);
```

```cpp
if (world.hit(r, interval(0.001, infinity), rec)) {
	ray scattered;
	color attenuation;

	if (rec.mat->scatter(r, rec, attenuation, scattered))
		return attenuation * ray_color(scattered, depth-1, world);

	return color(0,0,0);
}
```

```cpp
color camera::ray_color(const ray& r, int depth, const hittable& world) const {
    if (depth <= 0)
        return color(0, 0, 0);
        
    hit_record rec;

    if (world.hit(r, interval(0.001, infinity), rec)) {
        ray scattered;
        color attenuation;

        if (rec.mat->scatter(r, rec, attenuation, scattered))
            return attenuation * ray_color(scattered, depth-1, world);

        return color(0,0,0);
    }

    vec3 unit_direction = unit_vector(r.direction());
    auto a = 0.5*(unit_direction.y() + 1.0);

    return (1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0);
}
```

# References

[^1]: Read more about [[proj_raytracing_vec3|color]] in context of this project.
[^2]: Read more about [[notes_publisher/docs/Projects/rayTracing/proj_raytracing_ray|ray]] in context of this project.
[^3]: Read more about [[mth101_04|lines]].
[^4]: Read more about [[M_Function|functions]].
[^5]: Read more about [[10. Introduction to vectors|vectors]].
[^6]: Read more about [[mth101_01|intervals]].