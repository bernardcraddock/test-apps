print('\n*** Start tuples - an immutable ordered collection used to store multiple items in a single variable..\
\ninflexibe but fast\
\ntuple() parentheses ordered and immutable collection of items\
\nlist[] square brackets ordered and mutable collection of items\
\nset{} curly braces unordered and mutable collection of unique items\
\ndict{key: value} curly braces unordered and mutable collection of key-value pairs')

my_dict_car = {
  # key must be unique
    'make': 'Ford',
    'model': 'Mustang',
    'year': 1964,
    'price': '90k',
    'engine': ['v6', 'v8', 'v12'],                          #<-- list within a dict key must be unique and can be just about anything
    (1,2,'3'): ['v6', 'v8', 'v12']                          #<-- list within a dict key must be unique and can be just about anything
}

my_tuple_car = ('Ford', 'Mustang', 1964, '90k')


# writing too does't work reading from does
print('\nmy_tuple_car:', my_tuple_car)
print('slicing:', my_tuple_car[0:4:1])
print('Mustang' in my_tuple_car)
print('mustang' in my_tuple_car)                            #<-- False as case sensitive
print('White' in my_tuple_car)                              #<-- False as missing

print('\nmy_dict_car:', my_dict_car)
print('my_dict_car.items():', my_dict_car.items())
print('my_dict_car.[make]:', my_dict_car['make'])
print('my_dict_car.[make]:', my_dict_car['engine'][2])
print('my_dict_car.[1]:', my_dict_car[(1,2,'3')])           #<-- display whole list
print('my_dict_car.[1]:', my_dict_car[(1,2,'3')][2])        #<-- display 3rd index probably never use

print('\n*** Continue tuple - methods count() and index()')
my_new_tuple_car = my_tuple_car[0:3]
print('\nmy_new_tuple_car[0:3]:', my_new_tuple_car)

x,y,z, *other = (1,2,3,4,5,6,7,8,9)
print(other)

my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 5, 55, 5)
print(my_tuple.count(5))
print(my_tuple.index(5))
print(len(my_tuple))

