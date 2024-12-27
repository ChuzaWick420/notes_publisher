# Window Manager

`Window Manager` contains a `#!cpp sf::RenderWindow` object on which we will be drawing our rendered images.  
The object which is rendered is actually a `#!cpp sf::Sprite`, which based on a `#!cpp sf::Texture`, containing a `#!cpp sf::Image`.  
![[Proj_raytracing_sprites.svg]]  
/// caption  
image to window pipeline  
///

There can be a mismatch between the `sprite` and the `window` size (not the aspect ratios though because both determine the other factor of their dimension based on the aspect ratio).  
We can _scale_ the `sprite` up or down to fit in the `window` perfectly.  
![[proj_raytracing_scaling_image.svg]]  
/// caption  
Sprite being scaled to the window  
///

To find this `scalar` value, we are dividing either dimension of the `window` by the `sprite`.

```cpp
float scalar = float(u_width) / img->getSize().x;
```

Rest of the `#!cpp display()` function is pretty simple.

```cpp
void Window_manager::display(const sf::Image* const img) {

    sf::Texture T_img;
    T_img.loadFromImage(*img);

    sf::Sprite S_img(T_img);

    float scalar = float(u_width) / img->getSize().x;
    S_img.scale(sf::Vector2f(scalar, scalar));

    // debug
    std::cout << "Img: " << img->getSize().x << "x" << img->getSize().y << std::endl;
    std::cout << "Window: " << u_width << "x" << u_height << std::endl;

    while(R_window.isOpen()) {

        sf::Event event;
        while (R_window.pollEvent(event)) {
            if(event.type == sf::Event::Closed)
                R_window.close();
        }

        R_window.clear(clr_bg_color);
        R_window.draw(S_img);
        R_window.display();
    }
}
```