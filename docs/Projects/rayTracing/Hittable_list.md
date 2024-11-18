# Hittable_list

## Members

### `#!cpp std::vector<shared_ptr<hittable>> objects`

A `vector` (list) containing the objects.

## Methods

### Constructors

#### `#!cpp hittable_list()`

Does nothing.

#### `#!cpp hittable_list(shared_ptr<hittable>)`

Adds the object to the list.

```cpp
hittable_list::hittable_list(shared_ptr<hittable> object) {
    add(object); 
}
```

### Normal

#### `#!cpp void clear()`

Clears the list.

#### `#!cpp void add(shared_ptr<hittable>)`

Adds the object to the list.

```cpp
void hittable_list::add(shared_ptr<hittable> object) {
    objects.push_back(object);
}
```

#### `#!cpp bool hit(const ray& r, interval ray_t, hit_record& rec) const override`

Iterate over the `objects`.

```cpp
for (const auto& object : objects) {}
```

With each iteration, find a hit and narrow down the `interval`[^1]

```cpp
if (object->hit(r, interval(ray_t.min, closest_so_far), temp_rec)) {
	hit_anything = true;
	closest_so_far = temp_rec.t;
	rec = temp_rec;
}
```

Therefore, full code looks something like

```cpp
bool hit(const ray& r, interval ray_t, hit_record& rec) const override{

	hit_record temp_rec;
	bool hit_anything = false;
	auto closest_so_far = ray_t.max;

	for (const auto& object : objects) {
		if (object->hit(r, interval(ray_t.min, closest_so_far), temp_rec)) {
			hit_anything = true;
			closest_so_far = temp_rec.t;
			rec = temp_rec;
		}
	}

	return hit_anything;
}
```

## References

[^1]: Read more about [[notes_publisher/docs/Projects/rayTracing/Interval|interval]] in context of this project.