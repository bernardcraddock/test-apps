// Filename: main.mm
#include <iostream>

// Define a C++ class
class MyClass {
public:
    void sayHello() {
        std::cout << "Hello from C++!" << std::endl;
    }
};


int main() {
    // Create an instance of the C++ class and call its method
    MyClass myClass;
    myClass.sayHello();
}
