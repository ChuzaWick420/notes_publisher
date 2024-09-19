```cpp
#include <iostream>
#include "graphics.h"

#define PI 3.14

enum {
    UP = 1, DOWN, LEFT, RIGHT
} directions;

class Car {

    public:
        Car(int x) : size(x) {}

        ~Car() {
            delete[] (*this).wheels;
        }

        void allocate();

    private:
        static int size = 0;
        int wheels* = nullptr;
};

void Car::allocate(){
    this->wheels = new int[4];
}

int main () {
    int x = 10;
    float y = 20.0f;

    Car obj(5);

    std::cout << "hello world" << std::endl;

    return 0;
}
```
