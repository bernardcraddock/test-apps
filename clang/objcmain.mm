// Filename: main.mm
#include <iostream>
#import <Foundation/Foundation.h>

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
    // Create an instance of the Objective-C class and call its method
    MyObjCClass *myObjCClass = [[MyObjCClass alloc] init];
    [myObjCClass sayHello];

    return 0;
}
