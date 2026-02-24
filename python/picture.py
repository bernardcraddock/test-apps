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