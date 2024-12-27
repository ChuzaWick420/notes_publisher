# Scene

`Scene` deep inside, is a container over `hittable_list` class with a `#!cpp create_scene()` function which iterates over a list of objects which are later passed to `#!cpp Hittable_list::add()`.

```cpp
void Scene::setup(std::vector<std::shared_ptr<Hittable>> objects) {
    vec_Obj_objects = objects;
}
```

```cpp
Hittable_list& Scene::create_scene() {

    for (auto itr = vec_Obj_objects.begin(); itr != vec_Obj_objects.end(); itr++) {
        HL_world.add(*itr);
    }

    return HL_world;
}
```