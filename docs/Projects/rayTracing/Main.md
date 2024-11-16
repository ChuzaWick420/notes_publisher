# Main

## `#!cpp main()`

```cpp
#include "./headers/vec3/vec3.hpp"
#include "./headers/sphere/sphere.hpp"
#include "./headers/hittable_list/hittable_list.hpp"
#include "./headers/camera/camera.hpp"

#include "./headers/main_header.hpp"

int main () {

    // World
    hittable_list world;

    world.add(make_shared<sphere>(point3(0,0,-1), 0.5));
    world.add(make_shared<sphere>(point3(0,-100.5,-1), 100));

    camera cam;

    cam.aspect_ratio = 16.0 / 9.0;
    cam.img_width = 1024;
    cam.samples_per_pixel = 100;
    cam.max_depth = 50;

    cam.render(world);

    return 0;
}

```
