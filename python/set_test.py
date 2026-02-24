print('\n*** Start sets part 1 - unordered and mutable collection of unique values\
\ntuple() parentheses ordered and immutable collection of items\
\nlist[] square brackets ordered and mutable collection of items\
\nset{} curly braces unordered and mutable collection of unique items\
\ndict{key: value} curly braces unordered and mutable collection of key-value pairs\n')

print('\nmy_set')
my_set = {10, 9, 8, 1, 2, 3, 7, 6, 5, 4, 10}         # <-- 2 * 10
print('my_set:', my_set)                            # <-- diplays 1 * 10 (because is unique) no errors
print('my_set.remove(10):', my_set.remove(10))     # <-- removes all 10s
print('my_set:', my_set)
my_set.add(12)
print('my_set.add(12)', my_set)

print('\nmy_list set and my_new_set')
my_list = [10, 9, 8, 1, 2, 7, 6, 5, 4, 10]
print('my_list', my_list)
print('my_set.add(3)', my_set)
my_new_set = set(my_list)                           # <-- this isself sorting
print('set(my_list) and self sorted', my_new_set)
my_new_set.add(12)
my_new_set.add(3)
print('my_new_set.add(3 and 12)', my_new_set)


print('\n*** Continue sets part 2\
\n.difference()         - Returns a set containing the difference between two or more sets\
\n.difference_update()  - Removes the items in this set that are also included in another, specified set\
\n.discard()            - Remove the specified item\
\n.intersection()       - Returns a set, that is the intersection of two or more sets\
\n.isdisjoint()         - Returns whether two sets have a intersection or not\
\n.issubset()           - Returns whether another set contains this set or not\
\n.issuperset()         - Returns whether this set contains another set or not\
\n.union()              - Return a set containing the union of sets')

my_set   = {1, 2, 3, 4, 5, 11, 12}
your_set = {   2, 3, 4, 5, 6, 7, 8, 9, 10}

print('\nmy_set', my_set)
print('your_set', your_set)

print('\nmy_set.difference:', my_set.difference(your_set))
# 1. returns None shows it discarded the value and modifies the set
# 2. print the set shows remaining values
print('my_set.discard(1)', my_set.discard(1))
print('my_set.difference:', my_set.difference(your_set))
print('my_set', my_set)
# remove the items in this set that also exist in the other set
print('my_set.difference_update(your_set)', my_set.difference_update(your_set))
print('my_set', my_set)


my_new_set   = {1, 3, 5, 7, 9, 11, 13}
your_new_set = {1, 2, 4, 6, 8, 10, 12, 13}

print('\nmy_new_set', my_new_set)
print('your_new_set', your_new_set)

# Returns a set, that is the intersection of two or more sets
print('\nmy_new_set.intersection(your_new_set)', my_new_set.intersection(your_new_set))

# Returns whether two sets have an intersection or not
# Return True if no items in set x is present in set y:
print('my_new_set.isdisjoint(your_new_set)', my_new_set.isdisjoint(your_new_set))


my_set   = {2, 4, 6, 8, 10, 12}
your_set = {1, 3, 5, 7, 9, 11}
print('\nmy_set  ', my_set)
print('your_set', your_set)
# Return True if no items in set x is present in set y: Nothing in common
print('my_set.isdisjoint(your_set)', my_set.isdisjoint(your_set))
print('your_set.isdisjoint(my_set)', your_set.isdisjoint(my_set))


my_set   = {1, 3, 5, 7, 9,     11, 5, 10, 12}
your_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11}
print('\nmy_set  ', my_set)
print('your_set', your_set)
# Returns true/false am i a subset
print('my_set.issubset(your_set)', my_set.issubset(your_set))
print('your_set.issubset(my_set)', your_set.issubset(my_set))
# Returns true/false am i a superset
print('my_set.issuperset(your_set)', my_set.issuperset(your_set))
print('your_set.issuperset(my_set)', your_set.issuperset(my_set))
# Returns union of both a and b remove dups so both are same
print('my_set.union(your_set)', my_set.union(your_set))
print('your_set.union(my_set)', your_set.union(my_set))
print('my_set | your_set', my_set | your_set )  # <-- same as union

#print('\nyour_set.difference:', your_set.difference(my_set))
#print('your_set.discard(4)', your_set.discard(4))
#print('your_set', your_set)


#x = my_set.difference(your_set)
#print('x', x)
#my_set.discard(x)
#print('my_set', my_set)