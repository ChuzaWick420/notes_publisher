# C++

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

# Python

```Python
# Simple function decorator
def log_execution(func):
    def wrapper(*args, **kwargs):
        print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Finished {func.__name__}")
        return result
    return wrapper

# Decorator with arguments to repeat a function call n times
def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)
        return wrapper
    return decorator

# Using decorators with functions in the syntax sugar example
@log_execution
def multiply(x, y):
    return x * y

@repeat(3)
@log_execution
def greet(name):
    print(f"Hello, {name}!")

@log_execution
def say_hello():
    print("Hello!")

# List comprehension
squares = [x**2 for x in range(10)]

# Dictionary comprehension
squares_dict = {x: x**2 for x in range(10)}

# Set comprehension
unique_squares = {x**2 for x in range(10)}

# Generator expression
squares_gen = (x**2 for x in range(10))

# Tuple unpacking
a, b, c = (1, 2, 3)

# Extended unpacking
first, *middle, last = range(5)

# F-strings for formatting
name = "Python"
greeting = f"Hello, {name}!"

# Lambda function (inline function definition)
add = lambda x, y: x + y
result = add(5, 3)

# Ternary conditional expression
is_even = "Even" if result % 2 == 0 else "Odd"

# Using `*` to unpack function arguments
args = (2, 3)
product = multiply(*args)

# Using `**` to unpack keyword arguments
def print_info(name, age):
    print(f"{name} is {age} years old.")

info = {"name": "Alice", "age": 30}
print_info(**info)

# Chained comparison
x = 10
is_in_range = 5 < x < 15

# Context manager (with statement)
with open("example.txt", "w") as f:
    f.write("Hello, World!")

# Enumerate in loops
for idx, value in enumerate(squares):
    print(f"Index {idx} has value {value}")

# Zip for iterating over multiple iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    print(f"Number: {num}, Character: {char}")

# Using decorated functions
say_hello()
greet("Python")
```

# Rust

```rust
// Deriving traits automatically (like Debug, Clone)
#[derive(Debug, Clone)]
struct Point {
    x: i32,
    y: i32,
}

// Implementing methods for a struct
impl Point {
    // Associated function (similar to a static method in other languages)
    fn new(x: i32, y: i32) -> Self {
        Self { x, y }
    }

    // Method that takes self by reference
    fn distance_from_origin(&self) -> f64 {
        ((self.x.pow(2) + self.y.pow(2)) as f64).sqrt()
    }

    // Method that consumes self
    fn move_to_origin(self) -> Self {
        Self { x: 0, y: 0 }
    }
}

// Generic function with trait bounds
fn print_distance<T: Into<f64>>(distance: T) {
    println!("Distance: {}", distance.into());
}

// Pattern matching and destructuring
fn match_point(point: &Point) {
    match point {
        Point { x, y: 0 } => println!("Point lies on the X-axis at x = {}", x),
        Point { x: 0, y } => println!("Point lies on the Y-axis at y = {}", y),
        Point { x, y } => println!("Point is at ({}, {})", x, y),
    }
}

// Using closures
fn apply_closure<F>(closure: F) -> i32
where
    F: Fn(i32) -> i32,
{
    closure(5)
}

// Function overloading using trait implementations
trait Shape {
    fn area(&self) -> f64;
}

struct Circle {
    radius: f64,
}

impl Shape for Circle {
    fn area(&self) -> f64 {
        std::f64::consts::PI * self.radius.powi(2)
    }
}

struct Square {
    side: f64,
}

impl Shape for Square {
    fn area(&self) -> f64 {
        self.side.powi(2)
    }
}

// Operator overloading using traits
use std::ops::Add;

impl Add for Point {
    type Output = Point;

    fn add(self, other: Point) -> Point {
        Point {
            x: self.x + other.x,
            y: self.y + other.y,
        }
    }
}

// Option and Result types with combinators (map, and_then)
fn divide(a: i32, b: i32) -> Option<f64> {
    if b != 0 {
        Some(a as f64 / b as f64)
    } else {
        None
    }
}

// Iterator combinators
fn iterator_example() {
    let numbers = vec![1, 2, 3, 4, 5];
    let sum: i32 = numbers.iter().map(|x| x * 2).filter(|x| x % 3 == 0).sum();
    println!("Sum of doubled numbers divisible by 3: {}", sum);
}

// Lifetimes
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() {
        s1
    } else {
        s2
    }
}

// Using macros for code generation
macro_rules! say_hello {
    () => {
        println!("Hello, Rust!");
    };
}

fn main() {
    // Struct instantiation and using derived traits
    let point1 = Point::new(3, 4);
    println!("{:?}", point1); // Debug trait

    // Calling methods
    let distance = point1.distance_from_origin();
    println!("Distance from origin: {}", distance);

    let moved_point = point1.clone().move_to_origin();
    println!("Moved point: {:?}", moved_point);

    // Generic function with trait bounds
    print_distance(distance);

    // Pattern matching
    let point2 = Point { x: 0, y: 5 };
    match_point(&point2);

    // Closures
    let closure = |x| x * 2;
    println!("Closure result: {}", apply_closure(closure));

    // Function overloading via traits
    let circle = Circle { radius: 2.0 };
    let square = Square { side: 3.0 };
    println!("Circle area: {}", circle.area());
    println!("Square area: {}", square.area());

    // Operator overloading
    let point3 = Point::new(1, 2);
    let point4 = Point::new(3, 4);
    let sum_point = point3 + point4;
    println!("Summed point: {:?}", sum_point);

    // Option combinators
    if let Some(result) = divide(10, 2) {
        println!("Division result: {}", result);
    } else {
        println!("Division by zero");
    }

    // Iterator combinators
    iterator_example();

    // Lifetimes
    let string1 = String::from("long string");
    let string2 = "short";
    let result = longest(&string1, string2);
    println!("Longest string: {}", result);

    // Using macros
    say_hello!();
}
```

# Javascript

```js
// Arrow functions
const add = (a, b) => a + b;
const greet = name => `Hello, ${name}!`;

// Template literals
const name = "JavaScript";
const greeting = `Welcome to the world of ${name}!`;

// Destructuring assignment
const point = { x: 10, y: 20 };
const { x, y } = point;
const [first, second] = [1, 2];

// Default parameters
const multiply = (a, b = 1) => a * b;

// Rest parameters
const sum = (...numbers) => numbers.reduce((acc, curr) => acc + curr, 0);

// Spread operator
const arr1 = [1, 2, 3];
const arr2 = [4, 5, 6];
const combined = [...arr1, ...arr2];

// Object property shorthand
const age = 25;
const person = { name, age };

// Computed property names
const propName = 'dynamicProp';
const obj = {
    [propName]: 'This is dynamic',
};

// Method shorthand
const objWithMethods = {
    value: 42,
    getValue() {
        return this.value;
    },
    setValue(newValue) {
        this.value = newValue;
    }
};

// Classes and class methods
class Animal {
    constructor(name) {
        this.name = name;
    }

    speak() {
        console.log(`${this.name} makes a noise.`);
    }

    static create(name) {
        return new Animal(name);
    }
}

// Inheritance
class Dog extends Animal {
    speak() {
        console.log(`${this.name} barks.`);
    }
}

// Promises
const asyncOperation = () => new Promise((resolve, reject) => {
    setTimeout(() => resolve('Operation Complete'), 1000);
});

asyncOperation()
    .then(result => console.log(result))
    .catch(error => console.error(error));

// Async/Await
const fetchData = async () => {
    try {
        const response = await fetch('https://api.example.com/data');
        const data = await response.json();
        console.log(data);
    } catch (error) {
        console.error('Error fetching data:', error);
    }
};

// For...of loop
const iterable = [10, 20, 30];
for (const value of iterable) {
    console.log(value);
}

// Map and Set
const map = new Map([
    ['key1', 'value1'],
    ['key2', 'value2']
]);
const set = new Set([1, 2, 3, 2]);

// Proxy
const target = {};
const handler = {
    get: (obj, prop) => prop in obj ? obj[prop] : 'Property not found'
};
const proxy = new Proxy(target, handler);
console.log(proxy.someProperty); // Property not found

// Modules (import/export)
export const PI = 3.14;
export function calculateCircumference(radius) {
    return 2 * PI * radius;
}

// Importing (in another file)
// import { PI, calculateCircumference } from './path-to-module';

// Optional chaining
const person = { address: { city: 'New York' } };
const city = person.address?.city; // New York

// Nullish coalescing operator
const value = null ?? 'default'; // 'default'

// Array and object methods with arrow functions
const numbers = [1, 2, 3, 4];
const doubled = numbers.map(num => num * 2);
const filtered = numbers.filter(num => num % 2 === 0);
console.log(doubled); // [2, 4, 6, 8]
console.log(filtered); // [2, 4]

// Short-circuit evaluation
const logMessage = (message) => console.log(message);
true && logMessage('This will log.');
false && logMessage('This will not log.');

// Immediately Invoked Function Expression (IIFE)
(() => {
    console.log('This runs immediately!');
})();
```

# x86asm

```
; x86 Assembly example demonstrating common idioms

section .data
    msg db 'Hello, x86 Assembly!', 0  ; null-terminated string

section .bss
    num resb 4  ; reserve 4 bytes for an integer

section .text
    global _start

_start:
    ; Move immediate values into registers
    mov eax, 5             ; Load 5 into EAX
    mov ebx, 10            ; Load 10 into EBX

    ; Add, subtract, multiply, and divide
    add eax, ebx           ; EAX = EAX + EBX (15)
    sub ebx, eax           ; EBX = EBX - EAX (-5)
    imul eax, ebx          ; EAX = EAX * EBX (-75)
    idiv ebx               ; EAX = EAX / EBX (division by EBX, remainder in EDX)

    ; Comparison and conditional jumps
    cmp eax, ebx           ; Compare EAX with EBX
    je equal_label         ; Jump if equal
    jl less_than_label     ; Jump if less than

    ; Loop example
    mov ecx, 10            ; Set counter to 10
loop_start:
    dec ecx                ; Decrement ECX
    jnz loop_start         ; Jump if ECX is not zero

    ; Function call and return
    call print_message     ; Call a function to print a message
    jmp exit               ; Jump to exit

equal_label:
    ; Handle equality case
    ; ...

less_than_label:
    ; Handle less than case
    ; ...

print_message:
    ; Print message to stdout (Linux system call)
    mov eax, 4             ; sys_write system call number
    mov ebx, 1             ; File descriptor (stdout)
    mov ecx, msg           ; Pointer to message
    mov edx, 19            ; Length of message
    int 0x80               ; Interrupt to make system call
    ret                    ; Return from function

exit:
    ; Exit program (Linux system call)
    mov eax, 1             ; sys_exit system call number
    xor ebx, ebx           ; Exit code 0
    int 0x80               ; Interrupt to make system call
```

> [!note]- A note  
> Hi

> [!tip]- A tip  
> Hi

> [!example]- An example  
> Hi

> [!quote]- A quote  
> Hi

> [!warning]- A warning  
> Hi

> [!info]- An info  
> Hi

> [!question]- A question  
> Hi

> [!success]- A success  
> Hi

> [!todo]- A todo  
> Hi

> [!failure]- A failure  
> Hi

> [!error]- An error  
> Hi

> [!bug]- A bug  
> Hi

> [!warning]- 3 Notifications
> 
> > [!bug]- A bug  
> > Oh no, a logical error
> 
> > [!error]- A fatal error  
> > Ran out of space
> 
> > [!failure]- Task Failed  
> > Resources Exhausted
> 
> > [!tip]- Fixes
> > - Eat
> > - Sleep
> > - Play
> > - Hardwork
> > - Repeat

```cpp hl_lines="4"
#include <iostream>

int main() {
	std::cout << "Hello World!" << std::endl; // (1)!
	return 0;
}
```

1. The `cout` objects is part of the `std` namespace.

The tradition  

??? Example  
	=== "Javascript"  
		```js  
		console.log("Hello World");  
		```  
	=== "Python"  
		```py  
		print("Hello World")  
		```
