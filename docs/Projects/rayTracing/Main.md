# Main

Our first task is to have a way to display whatever the heck we are trying to display.  
For that, I am using [SFML](https://github.com/SFML/SFML).

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

for(int i = 0; i < img_height; i++) {
	for (int j = 0; j < img_width; j++) {
		i_image.setPixel(j, i, pixel_grid[i][j]);
	}
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

    for(int i = 0; i < img_height; i++) {
        for (int j = 0; j < img_width; j++) {
            i_image.setPixel(j, i, pixel_grid[i][j]);
        }
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
        
		//clear previous frame
        window.clear(sf::Color::Green);

		//draw new frame
        window.draw(s_image);

		//display it
        window.display();
    }
}
```

A `ray tracer` is responsible for following tasks.

1. Shooting rays out of the eye.
2. Determining which objects are being hit by that ray at closest.
3. Determine the color of pixel to show on screen.

Now we need to know what a `ray`[^1] is.  

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

So our task is to smoothly transform each `color`[^2] component into the component of the other `color`,[^2] depending on some variable.  
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

This `function`[^4] returns the pixel color for each `ray`[^1] for the _sky_.

```cpp
vec3 unit_direction = unit_vector(r.direction());
```

There is a slight problem though  
![[unit _vec.svg]]  
The $y$ component of the `unit vector`[^3] is in $[-1, 1]$ so we need to modify some of our maths for it.  
![[unit_vec_2.svg]]  
So the `interval`[^5] we are working with is $[-1, 1]$ and we want it to be $[0, 1]$  
First thing to realize is that if we add $1$ to our input, the `interval`[^5] becomes  

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

The way we will be sending the `rays`[^1] is going to be opposite to the direction of $y$ component of `unit vector`.[^3]  
Since the direction is opposite, so the $W$ is replaced by $B$ and vise versa.

$$y(a) = (1 - h)W + hB$$

And this applies over all components of the `color`[^2]

```cpp
return (1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0);
```

```cpp
color ray_color(const ray& r) {
	vec3 unit_direction = unit_vector(r.direction());
    auto a = 0.5*(unit_direction.y() + 1.0);
    return (1.0-a)*color(1.0, 1.0, 1.0) + a*color(0.5, 0.7, 1.0);
}
```

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Ray|ray]] in context of this project.
[^2]: Read more about [[Vec3|colors]].
[^3]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/4. Lines/Lecture|lines]].
[^4]: Read more about [[notes_publisher/docs/Mathematics/Function/Content|functions]].
[^5]: Read more about [[notes_publisher/docs/University Notes/semester 1/MTH101 - Calculus and Analytical Geometry/1. Coordinates, Graphs, Lines/Lecture|intervals]].