class Person:
    def __init__(self, name, age, country, edu):
        self.name = name
        self.age = age
        self.country = country
        self.edu = edu

    def __lt__(self, other):
        return self.age < other.age

    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}, Country: {self.country} Edu: {self.edu}"


p1 = Person("John", 36, "Norway", "BSc")
p2 = Person("Sara", 35, "UK", "Msc")

if p1 < p2:
    print(f"{p1.name} is younger than {p2.name}")
else:
    print(f"{p2.name} is younger than {p1.name}")


def multiple_by_two(num):
    return num * 2


def sum(num1, num2):
    return num1 + num2


print(sum(20, 3))


print("\nFor Loop start: iterable using range")
my_range = range(1, 7)
for _ in my_range:
    print("\n", _)  # <-- throwaway where variable not required
    print(f"my_range")
    print(list(range(5)))
    print(set(range(6)))
    print(tuple(range(7)))
