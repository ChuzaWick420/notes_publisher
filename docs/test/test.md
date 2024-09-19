```cpp
#include <iostream>
#include "graphics.h"

#define PI 3.14

//single line comment
template <typename T>
void hi(T val) {
    std::cout << val << std::cout;
}

/*
Multi
Line
Comment
*/

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
        int dir = UP;
        int wheels* = nullptr;
};

void Car::allocate(){
    this->wheels = new int[4];
}

int main () {
    int x = 10;
    float y = 20.0f;

    Car obj(5);

    std::cout << "hello world \n";

    return 0;
}
```
