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

#### `#!cpp int samples_per_pixel`

#### `#!cpp int max_depth`

### Private

## Method

### Constructors

### Destructors

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

### Overloaded

### Static