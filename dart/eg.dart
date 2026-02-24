class Box<T> {
  T value;
  Box(this.value);
}

void main() {
  var intBox = Box<int>(10);
  print(intBox.value); // prints 10

  var stringBox = Box<String>('Hello');
  print(stringBox.value); // prints 'Hello'
}
