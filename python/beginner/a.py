x = ["apple", "banana", "cherry"]
print(type(x))
print(x)

x = ("apple", "banana", "cherry")
print(f'\n{type(x)}')
print(x)

x = 5
x = complex(x)
print(f'\n{type(x)}')
print(x)


car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"] = "red"
print(f'\ncar: {car}')
	
class Person:
  def __init__(self, name, age, country, edu):
    self.name = name
    self.age = age
    self.country = country
    self.edu = edu

  def __lt__(self, other):
    return self.age < other.age
  
  def __le__(self, other):
    return self.age <= other.age

  def __str__(self):
    return f"Name: {self.name}, Age: {self.age}, Country: {self.country}, Edu: {self.edu}"

p1 = Person("John", 45, "Norway", "BSc")
p2 = Person("Sara", 46, "UK", "MSc")

if p1.age < p2.age:
  print(f'{p1.name} at {p1.age} is younger than {p2.name} at {p2.age}')
else:
  print(f'{p1.name} at {p1.age} is same age or older than {p2.name} at {p2.age}')

if p1.age <= p2.age:
  print(f'{p1.name} at {p1.age} is same age or younger than {p2.name} at {p2.age}')
else:
  print(f'{p1.name} at {p1.age} is older than {p2.name} at {p2.age}')


# using __lt__
if p1 < p2:
  print(f'Using __lt__ {p1.name} at {p1.age} is younger than {p2.name} at {p2.age}')
else:
  print(f'Using __lt__{p1.name} at {p1.age} is same age or older than {p2.name} at {p2.age}')

# using __le__
if p1 <= p2:
  print(f'Using __le__ {p1.name} at {p1.age} is same age or younger than {p2.name} at {p2.age}')
else:
  print(f'Using __le__{p1.name} at {p1.age} is older than {p2.name} at {p2.age}')
