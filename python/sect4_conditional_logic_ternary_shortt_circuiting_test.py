print('\n*** Start Section 4 Basics - ternary operator and short circuiting with key words\
\ntuple() parentheses ordered and immutable collection of items\
\nlist[] square brackets ordered and mutable collection of items\
\nset{} curly braces unordered and mutable collection of unique items\
\ndict{key: value} curly braces unordered and mutable collection of key-value pairs\n')


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


### keywords if, elif, else, and, or ternary operator and short circuting conditional expression shortcuts
# note then is replaced by body indentation
# short-circuiting specific refers to the behavior of boolean operators (such as and and or) to stop evaluating 
# expressions as soon as the result is known.
x = 5
if x > 0 and x < 10:    # Since x > 0 is True, the second operand (x < 10) will be evaluated
    print("x is between 0 and 10")

y = -5
if y > 0 and y < 10:    # Since y > 0 is False, the second operand (y < 10) will not be evaluated and nothing is printed
    print("y is between 0 and 10")


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
# == (comparrison not assigment), != (not equal), > (greater than), < (less than) >=, <= etc are strictly spesking comparison 
# operators not logical https://www.w3schools.com/python/python_operators.asp

print('\nternary operator is conditional expression shorthand for if-else \
\nusage: conditional_if_true if condition else condition_if_else\n')

x = 5
y = 10
z = x*(2+1) 
print('x:', x, 'y:',y, 'z', z)

max_value = x*(2+1) if x*2+1 > y else y
print('max_value', max_value, 'if_condition',  x*(2+1) )

is_friend = False
messages = "my friend so messages allowed" if is_friend else "Make friends before sending messages"
print('messges:', messages)


print('\nshort circuiting specific to and, or')
or_condition = True if x > y or z > y else False
print('or_condition', or_condition, 'z', z)

# added multiple conditions keyword operators not (logical) and != (comparison) are logiclly same
and_condition = True if x < y and (z-x)-1 != y and not (z-x)-1 == y and z-x == y else False
print('and_condition', and_condition, '(z-x)-1', (z-x)-1)


print('\nshort circuiting using true and false')
is_Friend = True
is_User = False
elf_something =  True # False


print('is_Friend and is_User)', is_Friend and is_User)
if is_Friend and is_User:
  print('if/and condition is_Friend and is_User:', is_Friend and is_User)
elif elf_something:
  print('elf_something', elf_something)
else:
   print('else condition is_Friend and is_User:', is_Friend and is_User)

print('is_Friend or is_User',is_Friend or is_User)
if is_Friend or is_User:
  print('if/or condition is_Friend or is_User:', is_Friend or is_User)
elif elf_something:
  print('elf_something', elf_something)
else:
   print('else codition is_Friend or is_User:', is_Friend or is_User)


print('\nlogical operators and, not, or')
a = 'b'
b = 'b'
print('a' > 'b')
print('a' < 'b')
print(a == b)

# lowercase letters are considered greater than uppercase letters in lexicographic order.
# character 'a' (ASCII code 97) is compared to character 'A' (ASCII code 65). 
# Since ASCII code 97 > ASCII code 65 expression 'a' < 'A' evaluates to False
print('a' < 'A')

print('\nlogical operator exercise')
is_Magician = False
is_Master = True

if is_Magician and is_Master:
    print('You are a master magician')
elif is_Magician and not is_Master:       # <-- "and not" (bool) is clearer than or 
  print('at least your getting there')
else:
   print('you need master powers')
  