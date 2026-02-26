print('\n*** Start Section 4 Basics - Developer fundamentals')

'''
 Object Types
 dict{k/v} curly braces unordered and mutable collection of key-value pairs
 list[]    square brackets ordered and mutable collection of items
 set{}     curly braces unordered and mutable collection of unique items
 tuple()   parentheses ordered and immutable collection of items
 range()   range object (start, stop, skip=1) similar to a tuple 
'''

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

print('\nDeveloper fundamentals continue - nested functions with return\
\nwhich always exits the function regardless')

x = 10
y = 5
print(f'\nx: {x} y: {y}')

print('ZTM course')
def outer_func(num1, num2): 
  def inner_func(n1, n2):           # <-- defined not called so bypassed
    return n1 * n2
  return num1 + num2
print(f'outer_func(+) {outer_func(x, y)}')

def outer_func(num1, num2): 
  def inner_func(n1, n2):           # <-- defined and called
    return n1 * n2
  return inner_func(num1, num2)
print(f'outer_func internally call inner_func(*) {outer_func(x, y)}')

print('\nMine')
def outer_multiple(num1, num2):
  def inner_multiple(n1, n2):
    return n1 * n2
  return inner_multiple(num1, num2)
print(f'keyword outer/inner(10,5) {outer_multiple(10, 5)}')

print('\nMine continue - Nested functions are only accessible within the scope of the outer function in\
\nwhich they are defined.\
\nThe following is only working becuase it found and is calling the external my_other_multiply\
\however note its actually calling both the externl 1st and then internal versions and returning\
\neach so the final result is the final return - This is ugly code and here for leafrning purposes only')

def my_other_multiply(num1=6, num2=7):       # <-- default values overwritten by positional
  my_sum = sum([num1, num2])
  print(f'2 inside external my_other_multiply num1: {num1} + num2: {num2} = my_sum {my_sum}')
  return sum([num1, num2])                         # <-- if return must return something and not None

x = 11; y = 7
print(f'\nx: {x} y: {y}')

def outer_func(num1, num2):
  print(f'3 complet external my_other_multiply now inside outer_function num1: {num1} num2: {num2}')
  
  def my_other_multiply(n1, n2):
    result = n1 * n2
    print(f'5 inside  internal my_other_multiply n1: {n1} * n2: {n2} = {result} but force return {(x*y) * (x*y)}')
    return (x*y) * (x*y)
    
  print(f'4 calling internal my_other_multiply num1: {num1} num2: {num2}')
  return my_other_multiply(num1, num2)

print(f'1 fall through call outer_func(my_other_multiply(x: {x}, y: {y})')                                     
my_total = outer_func(
  my_other_multiply(x,y),
  my_other_multiply(x,y))
print(f'6 exited outer_function set my_total {my_total} should = {(x*y) * (x*y)}')


print('\nchatGPT')
def outer_function(a):
  def inner_function(b):
    return a * b                
  return inner_function(y)
my_total = outer_function(x)
print(f'total variable: {my_total}')
print(f'total direct: {outer_function(x)}')    

print('\nchatGPT continue\
\nNested functions are only accessible within the scope of the outer function in which they are defined. If you want to use a nested function outside of its outer function, you need to return it from the outer function and assign it to a variable. Here’s an example:')

def outer_func(num1, num2): 
    def inner_func(n1, n2):           
        return n1 * n2
    return inner_func

my_inner_func = outer_func(x, y)
my_total = my_inner_func(x, y)
print(f'my_total: {my_total} from my_inner_func my_inner_func')
print(f'my_inner_func value is memory address {my_inner_func}')



