# Camera

## Members

### Public

#### `#!cpp double aspect_ratio`

For the dimensions, $16 : 9$ is pretty common so we are going to use that.

```cpp
float aspect_ratio = 16.0f / 9.0f
```

But we will keep it $1.0$ for default.

#### `#!cpp int img_width`

The `width` of the image.

#### `#!cpp int samples_per_pixel`

Amount of samples per pixel for anti-aliasing.

#### `#!cpp int max_depth`

Maximum light bounces.

### Private

#### `#!cpp std::vector<sf::Color> pixel_grid`

A one dimensional array which is used like a 2D grid.

## Method

### `#!cpp int window_width = 1024`

Default `width` of the `window`.

### `#!cpp int img_height`

`Height` of the `window`.

### `#!cpp point3 center`

Center of the `camera` in space.

### `#!cpp point3 pixel00_loc`

Coordinates of the top left pixel.

### `#!cpp vec3 pixel_delta_u`

Horizontal gaps between `pixels`.

### `#!cpp vec3 pixel_delta_v`

Vertical gaps between `pixels`.

### `#!cpp double pixel_samples_scale`

A Scalar value for pixels sample.

### Normal

#### `#!cpp void initialize()`

Initializes the default conditions for `camera`.

```cpp
void camera::initialize() {
    //file_ptr.open("image.ppm");

    img_height = int(img_width / aspect_ratio);
    img_height = (img_height < 1) ? 1 : img_height;

    pixel_samples_scale = 1.0 / samples_per_pixel;

    pixel_grid = new sf::Color*[img_height];
 
    for (int i = 0; i < img_width; i++) {
        pixel_grid[i] = new sf::Color[img_width];
    }

    // Determine viewport dimensions.
    auto focal_length = 1.0;
    auto viewport_height = 2.0;
    auto viewport_width = viewport_height * (double(img_width)/img_height);

    // Calculate the vectors across the horizontal and down the vertical viewport edges.
    auto viewport_u = vec3(viewport_width, 0, 0);
    auto viewport_v = vec3(0, -viewport_height, 0);

    // Calculate the horizontal and vertical delta vectors from pixel to pixel.
    pixel_delta_u = viewport_u / img_width;
    pixel_delta_v = viewport_v / img_height;

    // Calculate the location of the upper left pixel.
    auto viewport_upper_left =
        center - vec3(0, 0, focal_length) - viewport_u/2 - viewport_v/2;
        pixel00_loc = viewport_upper_left + 0.5 * (pixel_delta_u + pixel_delta_v);
}
```

The `focal_length` variable controls the distance of `camera` from the `viewport`.  
![[focal_length.svg]]  
Here $f$ is the `focal_length`.  
We control the `aspect ratio` and `image_width` manually.

The value of `focal_length` and dimensions of `viewport` don't hold much value as long as they are both scaled equally.  
In the following figure, $\frac {V_h} 2$ is the `viewport_height` and $S$ is any random `scalar` value.  
![[viewport_dimensions.svg]]

The following variables `pixel_delta_u` and `pixel_delta_v` are represented in the following figure, represented by  

$$\vec {\Delta u}$$

$$\vec {\Delta v}$$

![[viewport.svg]]

The `viewport_upper_left` is given by  
![[viewport_upper_left.svg]]

Similarly, `pixel00_loc` is given by  
![[pixel00_loc.svg]]

#### `#!cpp void render(const hittable&)`

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

![[modulo.svg]]

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

#### `#!cpp void show_img()`

To display something, we need a `window`.  

```cpp
sf::RenderWindow window(sf::VideoMode(window_width, window_height), "Ray Tracing", sf::Style::Default);
```

Then we need some entity to be displayed on this `window`, which is going to be a `sprite`.

```cpp
window.draw(s_image)
```

Now the question arises, what the `sprite` contains?  
Well, a `texture`.

```cpp
sf::Sprite s_image(t_image);
```

Now how does the `texture` gets its data?  
From an `image`.

```cpp
sf::Texture t_image;
t_image.loadFromImage(i_image);
```

How does the `image` has the color data?  
From an array of `pixels`.

```cpp
sf::Image i_image;
i_image.create(img_width, img_height);

int index = 1;

for (auto pixel : pixel_grid) {
	int x = (index - 1) % img_width;
	int y = (index - 1) / img_width;
	i_image.setPixel(x, y, pixel);

	index++;
}
```

Now we need to decide on the dimensions of `window` and `image`.  
![[scaling_image.svg]]  
It is obvious that we need to multiply a `scalar` value to the `image`'s dimensions to make it fit inside the `window`.  
This `scalar` is

```cpp
float scalar = window_width / img_width;
```

But we are losing some data due to the `/` operator.  
To make sure we get all decimal points (well most of them), we are going to cast it.

```cpp
float scalar = float(window_width) / img_width;
```

Also, since we are seeing things through the `camera` lens, it would make sense to put the display stuff inside `camera`.

```cpp
void camera::show_img() {

    int window_height = window_width / aspect_ratio;

    // Window to render image on
    sf::RenderWindow window(sf::VideoMode(window_width, window_height), "Ray Tracing", sf::Style::Default);

    float scalar = float(window_width) / img_width;

    //creates an image
    sf::Image i_image;
    i_image.create(img_width, img_height);

    int index = 1;

    for (auto pixel : pixel_grid) {
        int x = (index - 1) % img_width;
        int y = (index - 1) / img_width;
        i_image.setPixel(x, y, pixel);

        index++;
    }

    sf::Texture t_image;
    t_image.loadFromImage(i_image);

    sf::Sprite s_image(t_image);
    s_image.setScale(sf::Vector2f(scalar, scalar));

    while (window.isOpen()){
        sf::Event event;

        while(window.pollEvent(event)) {
            if (event.type == sf::Event::Closed)
                window.close();
        }

        window.clear(sf::Color::Green);

        window.draw(s_image);

        window.display();
    }
}
```

#### `#!cpp vec3 sample_square()`

Get's a random `vector`[^1] in a `square space` with dimensions  

$$1 \times 1$$

With `width` and `height` both ranging in $[-0.5, 0.5]$.

```cpp
vec3 camera::sample_square() const {
    return vec3(random_double() - 0.5, random_double() - 0.5, 0);
}
```

#### `#!cpp ray get_ray(int, int)`

![[sampling.svg]]  
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

#### `#!cpp color ray_color(const ray&, int, const hittable&)`

So our task is to smoothly transform each `color`[^1] component into the component of the other `color`,[^1] depending on some variable.  
For our purpose, we can use the $y$ component of the `ray`[^2] to play that role since it changes according to `height`.  
![[interpolation.svg]]  
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
![[unit _vec.svg]]  
The $y$ component of the `unit vector`[^5] is in $[-1, 1]$ so we need to modify some of our maths for it.  
![[unit_vec_2.svg]]  
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

#### `#!cpp vec3 sample_square()`

## References

[^1]: Read more about [[Vec3|color]] in context of this project.
[^2]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in context of this project.
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^4]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^5]: Read more about [[notes_publisher/docs/University Notes/semester 2/MTH301 - Calculus II/10. Introduction to vectors/Lecture|vectors]].
[^6]: Read more about [[1. Coordinates, Graphs, Lines|intervals]].