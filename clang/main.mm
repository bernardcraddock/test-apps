// Filename: main.mm
#include <iostream>
#import <Foundation/Foundation.h>

// Define a C++ class
class MyClass {
public:
    void sayHello() {
        std::cout << "Hello from C++!" << std::endl;
    }
};

// Define an Objective-C class
@interface MyObjCClass : NSObject
- (void)sayHello;
@end

@implementation MyObjCClass
- (void)sayHello {
    NSLog(@"Hello from Objective-C!");
}
@end

int main() {
    // Create an instance of the C++ class and call its method
    MyClass myClass;
    myClass.sayHello();

    // Create an instance of the Objective-C class and call its method
    MyObjCClass *myObjCClass = [[MyObjCClass alloc] init];
    [myObjCClass sayHello];

    return 0;
}
