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