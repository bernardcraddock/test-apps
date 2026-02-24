print('\n*** Continued  list which essentially are ordered index value use when order is important\
\ni.e queue inline of which following is not good example\
\n\ntuple()          - parentheses ordered and immutable collection of items\
\nlist[]           - square brackets ordered and mutable collection of items\
\nset{}            - curly braces unordered and mutable collection of unique items\
\ndict{key: value} - curly braces unordered and mutable collection of key-value pairs\n')

my_list = [
{
  1: 'a',
  20: 'b',
  3: 'Old Canterbury Road',
  # following works as strings immutable therefore hashable however this is not good useage 
  '[100]': 'Old Canterbury Road',
  4: 'e',
  5: 'n',
  6: 'r',
  6: 'R',            # <-- works because it overwrites previous key/value
  7: 'd',
  8: [10, 20, 30, 40, 48],
  9: True,           # <-- works
  # following works but throws out print my_list[0][1], changing to [1][1] works, is ugly don't use
  True: True       
},
{
  1: 'a',
  20: 'b',
  3: 'Old Canterbury Road',
  4: 'e',
  5: 'r',
  5: 'R',            # <-- works because it overwrites previous key/value
  6: 'n',
  7: 'd',
  8: [10, 20, 30, 40, 49, 121]
}]

print('my_list indexed: ',
      my_list[0] [20], my_list[1] [4],  my_list[0] [6],  my_list[1] [6],
      my_list[1] [1],  my_list[1] [5],  my_list[0] [7],  my_list[1] [8] [5],
      my_list[0] ['[100]'], 'is',  my_list[0] [9]
     )
