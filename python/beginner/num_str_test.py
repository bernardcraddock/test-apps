# Fundamental Data types (Built In) and opertors
print('\n*** Start num and strgFundamental Data types (Built In) and opertors\
\ntuple()          - parentheses ordered and immutable collection of items\
\nlist[]           - square brackets ordered and mutable collection of items\
\nset{}            - curly braces unordered and mutable collection of unique items\
\ndict{key: value} - curly braces unordered and mutable collection of key-value pairs\n')

'''
# numbers
int
float
complex

# other fundamental
bool
None  # (null)
str
list
tuple
set
dict

# clasess -> custom types
# Specialised Data types Modules & Plugins / extensions

# numbers int float complex 
print('int')
print(type(6))
print( type(2 + 4 ))
print( type(4 - 2 ))
print( type(2 - 4 ))
print( type(2 * 4 ))

x = 5
x = complex(x)
print(f'\n{type(x)}')
print(x)

print('** power of int')
print( 2 ** 256)           

print('float')
print( 2 * 4.5 )

print('int division // rounded down')
print( 5 // 2)            # 2 int

print ('float division / ')
print( 5 / 2 )             # 2.5

print('modulo % (reamained of this division)')
print( 5 % 2 )             # 1 int

print( 5 % 3 )             # 1 int
print( type(5 % 3 ))

# math functions
print('round down')
print(round(3.125))
print(round(3.4))
print(round(3.4999))

print('round up')
print(round(3.5))

print('abs absolute value i.e no negatives')
print(abs(.5))
print(abs(-.5))
print(abs(.0005))
print(abs(-.0005))
print(abs(0.0005))
'''


print('\n*** Start operator precedence 1 brackets 2 power of ** 3 * and / 4 + and -')
print((20+3)-(20-3))

print('\n*** Continue operator lambda')
x = lambda a : a + 10
print(x(5)*x(15))

print('\n*** Continue operator lambda binary number')
print(bin(1))
print(bin(5))
print(bin(2 ** 256))
print(bin(5))
# print(int('0b101', 2))
# print(int(bin(5),2))


print('\n*** Start complex numbers')
x = 3 + 4j
y = 5 - 2j
z = x + y
print(z)

print('\n*** Start constants PI')
# public start with word
# private start with _ (underscore)
# constants
PI = 3.14
_user_iq = 139
_user_age = ( _user_iq / 10)
print('My IQ is',
       + _user_iq, 'I am', 
       + _user_age, 'years old, age times PI is',
       + _user_age * PI)

# following exmaple i don't need the plur + sign
print('My IQ is',  
      _user_iq, 'I am', 
      _user_age, 'years old (', _user_age, '*', PI,') = ', 
      _user_age * PI )


print('\n*** Start dunnda __ functions')
# dunnda __
def my_function(x):
  return x * x # <-  returns square of x

_result = my_function(5)
print('my_function', _result)

_a, _b, _c = 'A', 5 ,10
print(_a, ',', _b, 'and', _c)


# # augmented assignment operator left of the = sign
print('\n*** Start augmented assignment operator left of the = sign')
_some_value = 5
_some_value += 2   # - * ** / //

_some_other_value = _some_value
_some_other_value **= 3
_third_value = _some_other_value / PI

print('some value', _some_value,
      '\nsome other value', _some_other_value, 
      '\nthird value', _third_value)


print('\n*** Start print string with quotes \'\'')
print('Str with quotes \'\"')
print(type('Str with quotes \'\"'))

# 3 single quotes
_long_string = '''
WOW
0 | 0 \'
-----
'''
print(_long_string)


# type conversion
print('\n*** Start type conversion')
a = str(100)
b = int(a)
c = float(b)
d = type(c)

print(a)
print(b)
print(c)
print(d)

print('\n*** continue type conversion number as string cast to int and float')
# Str concatenation
print(str(125.987))
print(type(str(125.987)))

print(int(str(125)))
print(type(int(str(125))))

print(float(str(125.987)))
print(type(float(str(125.987))))


# escape sequence
print('\n*** Start escape sequences')
todays_weather = '\tit\'s very sunny today \"isn\'t\" it sunny and bright\n\t new line tab\n new line no tab\t tab no newline'
print(todays_weather)


# # str concatenation
print('\n*** Start str concatentation and formatting')
#middle_name = input('Bernard enter your middle name? ' )
middle_name = str('Frank')
#last_name = input('Bernard enter your last name? ' )
last_name = 'Craddock'
age = 49

print('Hi Bernard ' + middle_name + ' ' + last_name + ' without formatting you are ' + str(age) + ' years old')

print('Hi Bernard {0} {1} using python2 formatting you are {2} years old'.format(middle_name, last_name, age))

print(f'Hi Bernard {middle_name} {last_name} using python3 formatting you are {age} years old')


print('\n*** Start str indexes [start:stop:stepover] strings are immutable')
# full_name_age = 'Bernard Frank Craddock 49'
full_name_age = str('Bernard ' + middle_name + ' ' + last_name + ' ' + str(age))
print(full_name_age)
print(full_name_age[0:7])
print(full_name_age[0:7:1])
print(full_name_age[0:7:2]) # Brad
# print(full_name_age[0:])
# print(full_name_age[1:])
# print(full_name_age[3:])
# print(full_name_age[:4])
# print(full_name_age[:7])
# print(full_name_age[8:13])
# print(full_name_age[::1])
# print(full_name_age[::2])
# print(full_name_age[-1])    # start at the end of the string
# print(full_name_age[::-1])  # reverse the string


# built in functions
print('\n*** Continue str indexes with Built in function')
full_name_age = full_name_age + ' James'       # <-- Bernard Frank Craddock 49 James 
print(len(full_name_age))                      # <-- len 31
print(full_name_age[0:len(full_name_age)])
print(full_name_age[0:31])


print('\n*** Start str with built in methods .find .capitalize .upper .isascii and .replace')
quote = "to be or not to be that is the question"
print(quote)
print(quote.find('that'))
print('center: ' + quote.center(50))
print('find position of \'that\' in string: ' + str(quote.find('that')))
print('Cap: ' + quote.capitalize())
print('upper: ' + quote.upper())
print('isascii: ' + str(quote.isascii()))
print('replace: ' + quote.replace('to', 'TO'))
#print(quote.replace('to', quote.upper(quote.find('to')))) # <-- nee to work on

second_quote = quote.replace('to', 'TO')
third_quote = second_quote.replace('or', 'OR')

print('quote:', quote)
print('2nd quote:', second_quote)
print('3rd quote:', third_quote)


# booleans
print('\n*** Start booleans')
is_cool = True
print('boolean: ', is_cool)


print('\n*** Start Type conversion using from/import with input')
from datetime import datetime
current_year = datetime.now().year
birth_year = input('Bernard enter your year of birth? ')
print(current_year - int(birth_year))
my_age = current_year - int(birth_year)
my_age = datetime.now().year - int(birth_year)     
my_age = datetime.now().year - float(birth_year)
my_age = datetime.now().year - bool(birth_year)  # mixing int, float and boolean all work
print(f'Bernard you are {my_age} years old boolean is true(1) false(0)')


print('\n*** Password checker using replace \'*\' * length')
user_name = input('Enter user? ' )
user_pass = input('Enter password? ')
x = user_pass.replace(user_pass, 'x-x-x-x')
y = print('*' * 10)
pass_length = len(user_pass)
hidden_pass = '*' * pass_length
print(f'user is {user_name} password {x} is {pass_length} chars long')
print(f'user is {user_name} password {hidden_pass} is {pass_length} chars long')
