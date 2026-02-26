print('\n*** Start Section 4 Basics - is vs == \
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


print('Difference betwen is and == ')

print('\nComparison operator == checks for equality between two objects.\
\nreturns true if objects referred to by the variables are equal.\
\n that is have the same value')
print( True == 1)                # True
print( '1' == 1)                 # False
print( [] == 1)                  # False
print( 10 == 10.0)               # True
print( [1,2,3] == [1,2,3])       # True
print( '[1,2,3]' == '[1,2,3]')   # True


print('\nkeyword is returns True if two variables point to the same memory space\
that is they are the same object\
\npython 3.8 Syntax Warning: \"is\" with a literal. Did you mean \"==\"?,\n thrown when\
\nidentity checks (is and is not) are used with certain types of literals (e.g. strings, number')
print( True is 1)           # False
print( '1' is 1)            # False
print( [] is 1)             # False 
print( [] is [])            # False becuase [] means assign new list
print( 10 is 10.0)          # False
print( 10 is 10)            # True because number 10 is in memory once
print( '1' is '1')          # True becuase str '1' isin memory once

print('\nChatGPT examples ')
a = [1, 2, 3]
b = a                        # <-- Same memory space
print(b == a)                # True
print(b is a)                # True becuase is (points) to same memory space

b = a[:]                     # makes a copy same as .copy()
print(b == a)                # True
print(b is a)                # False becuase b is different memory space

c = a.copy() 
print(c == a )                # True
print(c == a or c == b )      # True
print(c == a and c == b )     # True
print(c is b or c is a )      # False