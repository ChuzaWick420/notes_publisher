```cpp
#include <iostream>
#include <vector>
#include <memory>
#include <algorithm>
#include <tuple>

// Macro definition
#define PI 3.14159

// Enum class
enum class ShapeType { Circle, Rectangle };

// Template function
template <typename T>
T add(T a, T b) {
    return a + b;
}

// Base class declaration
class Shape {
public:
    // Virtual function (pure virtual for polymorphism)
    virtual double area() const = 0;

    // Virtual destructor
    virtual ~Shape() = default;

    // Static method (inside class)
    static constexpr const char* shapeType() {
        return "Shape";
    }
};

// Derived class declaration with method definition outside
class Circle : public Shape {
    double radius;
public:
    Circle(double r);   // Constructor declaration
    
    // Function defined outside the class
    double area() const override;

    // Static method defined outside the class
    static std::string typeName();
};

// Derived class declaration with constructor initializer list
class Rectangle : public Shape {
    double width, height;
public:
    Rectangle(double w, double h) : width(w), height(h) {}

    double area() const override {
        return width * height;
    }
};

// Constructor definition outside class (Circle)
Circle::Circle(double r) : radius(r) {}

// Method definition outside class (Circle)
double Circle::area() const {
    return PI * radius * radius;
}

// Static method definition outside class (Circle)
std::string Circle::typeName() {
    return "Circle";
}

int main() {
    // Smart pointers
    std::unique_ptr<Shape> circle = std::make_unique<Circle>(5.0);
    std::unique_ptr<Shape> rect = std::make_unique<Rectangle>(4.0, 6.0);

    // Template function usage
    std::cout << "Add PI + 3 = " << add(PI, 3) << std::endl;

    // Lambda expression (C++11)
    auto printArea = [](const std::unique_ptr<Shape>& shape) {
        std::cout << "Area: " << shape->area() << std::endl;
    };

    // Range-based for loop (C++11)
    std::vector<std::unique_ptr<Shape>> shapes;
    shapes.push_back(std::make_unique<Circle>(3.0));
    shapes.push_back(std::make_unique<Rectangle>(2.0, 5.0));

    for (const auto& shape : shapes) {
        printArea(shape);
    }

    // std::for_each with lambda
    std::for_each(shapes.begin(), shapes.end(), [](const auto& shape) {
        std::cout << "Shape area: " << shape->area() << std::endl;
    });

    // Structured bindings (C++17) with tuple
    std::tuple<int, double, std::string> myTuple = {1, 3.14, "Hello"};
    auto [intValue, doubleValue, stringValue] = myTuple;  // Structured binding
    std::cout << "Structured bindings: " << intValue << ", " << doubleValue << ", " << stringValue << std::endl;

    // Using decltype and auto
    decltype(circle) anotherCircle = std::make_unique<Circle>(4.0);
    std::cout << "Another Circle Area: " << anotherCircle->area() << std::endl;

    // Null pointer example
    Shape* nullShape = nullptr;  // C++11 nullptr

    if (nullShape == nullptr) {
        std::cout << "Shape pointer is null." << std::endl;
    }

    return 0;
}
```
