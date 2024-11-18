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