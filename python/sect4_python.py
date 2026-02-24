print('\n*** Start Section 4 Basics - Developer fundamentals')

'''
 Object Types
  dict{k/v} curly braces unordered and mutable collection of key-value pairs
  list[]    square brackets ordered and mutable collection of items
  set{}     curly braces unordered and mutable collection of unique items
  tuple()   parentheses ordered and immutable collection of items
  range()   range object (start, stop, skip=1) similar to a tuple 


tuple
  a built-in data type used to store a collection of items. It is similar to a 
  list, but with some important differences:
  Tuples are immutable, which means once created, their size and contents cannot 
  be changed. defined using parentheses () instead of square brackets [].

  my_tuple = (1, 2, 3)
  print(my_tuple) # (1, 2, 3)

Accessing elements
  print(my_tuple[0]) # 1
  print(my_tuple[1]) # 2
  print(my_tuple[2]) # 3


Built in data types
  Boolean Type:	  bool
  Binary Types:	  bytes, bytearray, memoryview
  Mapping Type:	  dict{key/val}
  None Type:	    NoneType
  Numeric Types:	int, float, complex
  Sequence Types:	list[], tuple(), range
  Set Types:	    set{}, frozenset
  Text Type:	    str - which are compared lexicographically, meaning it is based on 
                       the alphabetical order of the characters in the strings 'a' > 'b' is False


string Character ordering
  lowercase letters are considered greater than uppercase letters in lexicographic order.
  character 'a' (ASCII code 97) is compared to character 'A' (ASCII code 65). 
  Since ASCII code 97 > ASCII code 65 expression 'a' < 'A' evaluates to False


Truthy and Falsey
  Basis rules are:
      Values that evaluate to False are considered Falsy
      Values that evaluate to True are considered Truthy
  Falsy values as follows all others ar truthy:
     Constant: None, False
     Number Zero of any type: int(0), double(0.0), complex(0j)
     Empty Sequence & Collection: list[], dict{}, tuple(), set(), str'' and range(0)
Complete Lsit
  https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false


logical operators
  and, not, or
  == (comparrison), != (not equal), > (greater than), < (less than) >=, <= strictly speaking these are comparison 
  operators not logical https://www.w3schools.com/python/python_operators.asp


ternary operator
  a shorthand way of writing an if-else statement that evaluates to a single expression
  also known as a conditional expression.
  The syntax for a ternary operator in Python is:
  value_if_true if condition else value_if_false
'''

# Using if-else statement
x = 10
y = 9


if x < y:
  result = "is less than"
else:
  result = "is greater than or equal to"
print(f'{x} {result} {y}')

my_msg='Using ternary operator'
result = "is less than" if x < y else "is greater than or equal to"
print(f'{my_msg} {x} {result} {y}')


### Short Circuting
# conditional expression shortcuts
# specifically refers to the behavior of boolean operators (and, or) that stops evaluating expressions as soon 
# result is known.
#
x = 5
if x > 0 and x < 10:    # Since x > 0 is True, the second operand (x < 10) will be evaluated
  print(f'Short Circuting i.e and {x} > 0 is True will check 2nd operator')

y = -5
if y > 0 and y < 10:    # Since y > 0 is False, the second operand (y < 10) will not be evaluated and nothing is printed
  print(f'Short Circuting and {y} > 0 is False 2nd operator wont be evaluated')


print(f'\nComparison is v == ')
# == checks for equality between two objects/variables returns true if values are equal
# is keyword returns True if two variables point to the same memory space i.e same object
#
a = [1, 2, 3]
b = a                        # <-- Same memory space
#
print(b == a)                # True
print(b is a)                # True becuase is (points) to same memory space
# 
b = a[:]                     # makes a copy hence new memory space same as .copy()
print(b == a)                # True
print(b is a)                # False becuase b is different memory space
#
c = a.copy()
print(c == a )
print(c == a or c == b )      # True
print(c == a and c == b )     # True
print(c is b or c is a)      # False
#
# print( [] is [])            # False becuase [] means assign new list
# print( 10 is 10)            # True because number 10 is in memory once
# print( '1' is '1')          # True becuase str '1' isin memory once


### iterable
# iterable - can be any of dict{}, list[], set{} and tuple() collection
# to recursively iterate over each value in the iterable one by one
# iterate - to iterate over and check each item in the collection one by one
# dict 3 * key methods .items() .values() and  .keys() to iterate over a collection
#
my_sum = 0
my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]

for num in my_list:
  my_sum = num + my_sum
print(f'\niterate for my_sum {my_sum}')

my_user = {
  'name': 'Golem',
  'age': 1001,
  'can_swim': False
  }
#
print('iterate for key, value items')
for k, v in my_user.items():
  print(k, v)
#
# range(n)
# for _ in my_range:
#  print('\n',_)            # <-- throwaway where variable not required
#  print(my_range)
#  print(list(range(5)))
#  print(set(range(6)))
#  print(tuple(range(7)))


### enumerate
# a built-in function that allows you to loop over an iterable (list, set, string # etc ) and keep track of the current index of the item being processed. It # returns an iterator that generates pairs of the form (index, element).
#
my_list = ['apple', 'banana', 'cherry']
print(f'\nmy_list {my_list}')

for index, value in enumerate(my_list):
  print(f'enumerate over my_list using Index: {index}, Value: {value}')


print(f'\nfinding dups using for loop if and count() with and without using set')
numbers = [9, 1, 2, 3, 2, 5, 3, 9, 3, 5, 6, 3, 4, 5, 7]
print('numbers', numbers)
#
dups = []
for number in numbers:
  if numbers.count(number) > 1:
    if number not in dups:
      dups.append(number)
  
print(f'for loop nested if dups using count(number) without set {dups}')

#
dups = [number for number in numbers if numbers.count(number) > 1]
print(f'bracket enclosed number [for loop if count(number)] using sorted set {sorted(set(dups))}')

my_list = ['z', 'a', 'b', 'c', 'a', 'z', 'd', 'e', 'f', 'a', 'b', 'Z']
print(f'\nlist {my_list}')
dups = [char for char in my_list if my_list.count(char) > 1]
print(f'bracket enclosed char list [for loop if count(char) using sorted set {sorted(set(dups))}')


### while loop 
print('\nwhile condition is true loop') 
# else condition only executes when loop termniates normally (i.e., when loop 
# condition becomes False, can be used for code cleanup on successful termination 
# Can also break on a different condition, Big difference between for and  while loops
# you have to set, increment and ensure the loop terminates
#
my_list = ['a', 'b', 'c', 'a', 'd', 'e', 'f', 'a', 'b']
print(f'list: {my_list}\nlist length: {len(my_list)}')
print('set the condition i = 0')
i = 0 
while i < len(my_list):
  print(f'while {i} {my_list[i]}')
  i += 1
  if i >= len(my_list)+1:    # i >= 9 to break
    print(f'while {i} my_list[i] break')
    break
else:
  print(f'while/else {i} finished cleanly')


print('\nDeveloper fundamentals continue - functions xmas tree with params and arguments')

### function and Nested for loop 
# my_picture of a xmas tree
#
my_picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

def my_tree():
  for row in my_picture:
    for index in row:
      if index == 0:
        print(' ', end='')          # <-- Dont print new line \n
      else:
        print('*', end='')          # <-- dont print new line \n
    else:
      print(' ')                    # <-- print a new line nd of each row

def my_function(cnt, tree_func):    # <-- paramaters (define)
  for x in range(1,cnt):
    print(f'calling {tree_func} {x} of {cnt-1} times')
    my_tree()

my_function(4, 'my_tree')           # <-- arguments (call)

print(f'show memory location my_tree {my_tree}')
print(f'show memory location my_function {my_function}')


print('\nDeveloper fundamentals continue - functions positional, default and keyword arguments')

def my_function(cnt=6, func='default'):
  print(f'my_function {cnt} {func}')

my_function(4, 'positional')         # <-- positional
my_function(func='keyword', cnt=5)   # <-- keyword (keep them in order)
my_function(func='keyword-partial')  # <-- partial keyword
my_function()                        # <-- default
my_function(7)                       # <-- partial default


print('\nDeveloper fundamentals continue - functions with return')
def my_sum(num1, num2):
  print(f'summing {num1} + {num2}')
  return num1 + num2                         # <-- if return must return something and not None

def my_multiply(num1=6, num2=7):
  print(f'multiplying {num1} * {num2}')
  return num1 * num2                         # <-- if return must return something and not None

sum_tot = my_sum(4, 5)
multiply_tot = my_multiply()
print(f'sum_total= {sum_tot + multiply_tot}\n')
print(f'multiply_total= {sum_tot * multiply_tot}\n')
print(f'sum(multiply_total)= {my_sum(sum_tot * multiply_tot, 10)}\n')
print(f'multiple(multiply_total)= {my_multiply(sum_tot * multiply_tot)}\n')
print(f'Grand Total multiple(multiple(multiply_total))= {my_multiply(my_multiply(sum_tot * multiply_tot))}')

my_list = [1,2,3,4,5]
print(f'\nexample helper returning None using my_list {my_list}')
print(f'my_list.clear() {my_list.clear()}')  # <-- None

print('\nDeveloper fundamentals continue - nested functions return')

def outer_function(x):
    def inner_function(y):
        return x * y
    result = inner_function(2)
    return result
print(f'keyword outer(3) * inner(2): {outer_function(3)}')


def outer_function(x):
    def inner_function(y):
        return x * y
    return inner_function(4)
print(f'keyword outer(5) * inner(4): {outer_function(5)}')


def outer_multiple(num1, num2):
  def inner_multiple(n1, n2):
    return n1 * n2
  return inner_multiple(num1, num2)
print(f'keyword outer(10,5) is inner(10,5) {outer_multiple(10, 5)}')