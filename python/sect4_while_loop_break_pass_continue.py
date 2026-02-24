print('\n*** Start Section 4 Basics - while looops with\
\nbreak, continue an pass')


### Objecg Types
# dict{k/v} curly braces unordered and mutable collection of key-value pairs
# list[]    square brackets ordered and mutable collection of items
# set{}     curly braces unordered and mutable collection of unique items
# tuple()   parentheses ordered and immutable collection of items
# range()   range object (start, stop, skip=1) similar to a tuple 


### tuple
# a built-in data type used to store a collection of items. It is similar to a 
# list, but with some important differences:
# Tuples are immutable, which means once created, their size and contents cannot 
# be changed. defined using parentheses () instead of square brackets [].
#
# my_tuple = (1, 2, 3)
# print(my_tuple) # (1, 2, 3)
#
# Accessing elements
# print(my_tuple[0]) # 1
# print(my_tuple[1]) # 2
# print(my_tuple[2]) # 3


### Built in data types
# Boolean Type:	  bool
# Binary Types:	  bytes, bytearray, memoryview
# Mapping Type:	  dict{key/val}
# None Type:	    NoneType
# Numeric Types:	int, float, complex
# Sequence Types:	list[], tuple(), range
# Set Types:	    set{}, frozenset
# Text Type:	    str - which are compared lexicographically, meaning it is based on 
#                       the alphabetical order of the characters in the strings 'a' > 'b' is False


### string Character ordering
# lowercase letters are considered greater than uppercase letters in lexicographic order.
# character 'a' (ASCII code 97) is compared to character 'A' (ASCII code 65). 
# Since ASCII code 97 > ASCII code 65 expression 'a' < 'A' evaluates to False


### Truthy and Falsey
# Basis rules are:
#     Values that evaluate to False are considered Falsy
#     Values that evaluate to True are considered Truthy
# Falsy values as follows all others ar truthy:
#    Constant: None, False
#    Number Zero of any type: int(0), double(0.0), complex(0j)
#    Empty Sequence & Collection: list[], dict{}, tuple(), set(), str'' and range(0)
# Complete Lsit
# https://stackoverflow.com/questions/39983695/what-is-truthy-and-falsy-how-is-it-different-from-true-and-false


### logical operators
# and, not, or
# == (comparrison), != (not equal), > (greater than), < (less than) >=, <= strictly speaking these are comparison 
# operators not logical https://www.w3schools.com/python/python_operators.asp


### ternary operator
# a shorthand way of writing an if-else statement that evaluates to a single expression. 
# also known as a conditional expression.
# The syntax for a ternary operator in Python is:
# value_if_true if condition else value_if_false
#
# Using if-else statement
# if x < y:
#    result = "x is less than y"
# else:
#    result = "x is greater than or equal to y"
# print(result)
#
# Using ternary operator
# result = "x is less than y" if x < y else "x is greater than or equal to y"
# print(result)


### Short Circuting
# conditional expression shortcuts
# specifically refers to the behavior of boolean operators (and, or) that stops evaluating expressions as soon 
# result is known.
#
# x = 5
# if x > 0 and x < 10:    # Since x > 0 is True, the second operand (x < 10) will be evaluated
#    print("x is between 0 and 10")
#
# y = -5
# if y > 0 and y < 10:    # Since y > 0 is False, the second operand (y < 10) will not be evaluated and nothing is printed
#    print("y is between 0 and 10")


### Comparison is v == 
# == checks for equality between two objects/variables returns true if values are equal
# is keyword returns True if two variables point to the same memory space i.e same object
#
# a = [1, 2, 3]
# b = a                        # <-- Same memory space
#
# print(b == a)                # True
# print(b is a)                # True becuase is (points) to same memory space
# 
# b = a[:]                     # makes a copy hence new memory space same as .copy()
# print(b == a)                # True
# print(b is a)                # False becuase b is different memory space
#
# c = a.copy() 
# print(c == a )                # True
# print(c == a or c == b )      # True
# print(c == a and c == b )     # True
# print(c is b or c is a )      # False
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
# my_sum = 0
# my_list = [1, 2, 3, 4, 5, 6, 7, 8 ,9, 10]
# for num in my_list:
#  my_sum = num + my_sum
#
# my_user = {
#  'name': 'Golem',
#  'age': 1001,
#  'can_swim': False
# }
#
# print('\niterate for key, value items')
# for k, v in my_user.items():
# print(k, v)
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
# my_list = ['apple', 'banana', 'cherry']
#
#for index, value in enumerate(my_list):
#    print(f"Index: {index}, Value: {value}")

### Nested for loop 
# my_picture of a xmas tree
#
# my_picture = [
#  [0,0,0,1,0,0,0],
#  [0,0,1,1,1,0,0],
#  [0,1,1,1,1,1,0],
#  [1,1,1,1,1,1,1],
#  [0,0,0,1,0,0,0],
#  [0,0,0,1,0,0,0]
#]
#
#print('\ndraw my_picture')
#for row in my_picture:
#  for index in row:
#    if index == 0:
#      print(' ', end='')
#      continue
#    else: 
#      print('*', end='')
#      continue
#  else:
#    print('')


### while loop 
# while condition is true continue processing 
# else condition only executes when loop termniates normally (i.e., when loop 
# condition becomes False, can be used for code cleanup on successful termination 
# Can also break on a different condition, Big difference between for and  while loops
# you have to set, increment and ensure the loop terminates
#
# i = 0 
# while i < len(my_list):
#  print('while', my_list[i])
#  i += 1
#  if i == 6:
#    print(f' {i} c never be 6')
#    break
# else:
#    print("while finished normally")

print('\nwhile loops start:\
\nwhile condition is true continue procesing else false and stop:')

print('\nwhile count with else')
count = 0
while count <= 10:
  print(count)
  if count == 11:
    print(f'{count} == 10 will break')
    break
  count += 1
else:
  print(f'done counting {count} not <= 50')


print('\nwhile vs for loop')
my_list = [1, 2, 3, 4, 5]
for i in my_list:
  print('for', i)

print('\nfor loop pass statement')
for i in my_list:
  pass #<-- null operator when called used as placeholder when syntax requires something

print('\nwhile loop using index')
i = 0 
while i < len(my_list):
  print('while', my_list[i])
  i += 1
  if i == 6:
    print(f' {i} c never be 6')
    break
else:
    print("while finished normally")

while True:
  # my_input = input ('Continue [y/n]: ')
  my_input = 'n'
  if my_input == 'n' or my_input == 'N':
    print('exiting')
    break

print('\nwhile loop continue: - pass, continue and break')
n = 5
while n > 0:
    print(n)
    n -= 1
    if n == 4:
      print(f'{n} is 4 pass as still thinking of a response')
      pass
      
    if n == 3:
      print(f'{n} is 3 b4 continue')
      continue
      print(f'{n} is 3 aft continue')
      
    if n == 2:
      print(f'{n} is 2 time to break')
      break   
else:
    print("else while n loop finished normally")


print('\Nested for loop with my_picture')
my_picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]

print('\ndraw my_picture')
for row in my_picture:
  for index in row:
    if index == 0:
      print(' ', end='')
      continue
    else: 
      print('*', end='')
      continue
  else:
    print('')