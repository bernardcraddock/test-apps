
print('\n*** Start dict_methods-1 - dictionary unordered key(immuatble)/value pair i/e map\
used to hold information i.e emp attributes as such keys are mostly descriptive strings\
\ntuple()          - parentheses ordered and immutable collection of items\
\nlist[]           - square brackets ordered and mutable collection of items\
\nset{}            - curly braces unordered and mutable collection of unique items\
\ndict{key: value} - curly braces unordered and mutable collection of key-value pairs\n')

dictionary = {
  1: 'a',
  20: 'b',
  3: '121 Old Canterbury Road',
  # [100] '121 Old Canterbury Road',     <-- fails unhashable type keys must be immuatble
  '[100]': '121 Old Canterbury Road',  # <-- works because strings are immutable and therefore hashable 
  4: 'e',
  5: 'n',
  6: 'r',
  7: 'd',
  8: [10, 20, 30, 40, 49]
}
print('dictionary full: ', dictionary)

print('dictionary indexed: ',
      dictionary[20], dictionary[4], dictionary[6], dictionary[5], 
      dictionary[1],  dictionary[6], dictionary[7], dictionary['[100]'],
      dictionary[8][4]
      )



print('\n*** Continued dict_methods-1 (c) - dictionary methods my_cars')
my_car = {
  "make": "Ford",
  "model": "Mustang",
  "year": 1964,
  "price": "90k"
}

my_other_car = dict(brand="Jaguar", model="etype", year=1968, price="100k")

print('my_car.items()',      my_car.items())
print('my_car.get(model):',  my_car.get("model"))
print('my_car.get(price):',  my_car.get("price", "100k")) # <-- return this price only if dict value is None
my_car.update({"price": "120k"})
print('my_car.update price:', my_car)

print('my_other_car using dict:', my_other_car)
print('my_other_car.keys:', my_other_car.keys())
print('my_other_car.items:', my_other_car.items())
my_other_car.update({"price": "130k"})
my_other_car.update({"color": "red"})
my_other_car.update({"price-high": "150k"})
print('my_other_car.updated price/color(new):', my_other_car)
print('my_other_car.keys aft color:', my_other_car.keys())


print('\n*** Start dict_methods-2 - unordered immuatble key(/value pair i/e maps')

print('my_car: in keys and values total9 6*true 3*false') 
print('make' in my_car,
      'make' in my_car.keys(), 'Ford' in my_car.values(),
      'model' in my_car.keys(), 'Mustang' in my_car.values(),
      'year' in my_car.keys(), 1954 in my_car.values(),
      'color' in my_car.keys(), 'red' in my_car.values()
     )
print('my_car.(items) dict_items which are tuples\n', my_car.items())

print('\nmy_other_car: in keys and values total6 all true') 
print('brand' in my_other_car.keys(), 'Jaguar' in my_other_car.values(),
      'model' in my_other_car.keys(), 'etype' in my_other_car.values(),
      'color' in my_other_car.keys(), 'red' in my_other_car.values())
print('my_other_car.(items) dict_items which are tuples\n', my_other_car.items())


my_copy_car = my_car.copy()
print('\nmy_car.clear():', my_car.clear())
print('my_copy_car:', my_copy_car)
print('my_copy_car.pop(make) remove make:', my_copy_car.pop('make'))  # <-- returns the value that got removed
print('my_copy_car', my_copy_car)
print('my_copy_car.items()', my_copy_car.items())

my_other_copy_car = my_other_car.copy()
print('\nmy_other_car.clear():', my_other_car.clear())
print('my_other_copy_car:', my_other_copy_car)
# pop Remove and return the key value
print('my_other_copy_car.pop(model) remove model:', my_other_copy_car.pop('model'))  # <-- model etype
# popitem() Remove and return last inserted key-value pair
print('my_other_copy_car.popItem():', my_other_copy_car.popitem())                   # <-- price-high
print('my_other_copy_car.popItem():', my_other_copy_car.popitem())                   # <-- color
print('my_other_copy_car', my_other_copy_car)
print('my_other_copy_car.items()', my_other_copy_car.items())