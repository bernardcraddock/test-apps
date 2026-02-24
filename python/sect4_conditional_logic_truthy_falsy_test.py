print('\n*** Start Section 4 Basics - Conditional Logic with key words\
\ntuple() parentheses ordered and immutable collection of items\
\nlist[] square brackets ordered and mutable collection of items\
\nset{} curly braces unordered and mutable collection of unique items\
\ndict{key: value} curly braces unordered and mutable collection of key-value pairs\n'
      )

### Built in data types
# Boolean Type:	  bool
# Binary Types:	  bytes, bytearray, memoryview
# Mapping Type:	  dict{key/val}
# None Type:	    NoneType
# Numeric Types:	int, float, complex
# Sequence Types:	list[], tuple(), range
# Set Types:	    set{}, frozenset
# Text Type:	str

is_old_enough = False
has_license = False

# keywords if elif and else - same as if exists
if is_old_enough:
  # indentation is compiler directive, part of code block style is secondary
  print('is old enough')
elif has_license:
  print('has license')
else:
  print('No license and not old enough')

print('beyond if\n') # No indentation terminates compiler directive, i.e end of block

if is_old_enough and has_license:
  print('is old enough and has license')
elif has_license:
  print('has license but not old enough')
elif is_old_enough:
  print('is old enough but has no license')
else:
  print('No license and not old enough')
print('beyond 2nd if') # No indentation terminates compiler directive, you don't need line space but harder to read 


print('\n\n*** Continue Section 4 Basics - Truthy and Falsey\
\nBasis rules are:\
\n\tValues that evaluate to False are considered Falsy.\
\n\tValues that evaluate to True are considered Truthy.\
\n\nFalsy values can include:\
\n\tConstant: None, False\
\n\tNumber Zero of any type: int(0), double(0.0), complex(0j)\
\n\tEmpty Sequence & Collection: list[], dict{}, tuple(), set(), str'' and range(0)\
\n\nTruthy values can include:\
\n\tNon-empty sequences or collections (lists, tuples, strings, dictionaries, sets).\
\n\tNumeric values that are not zero.\
\n\tConstant: True')

print('\ntruthy')
is_old_enough = "Yes_No"   # converts to is_old_enough = bool("Yes_No")
has_license = 5            # converst to has_license = bool(5)

print('is_old_enough', is_old_enough, bool(is_old_enough))
print('has_license', has_license, bool(has_license))

print('\nFalsy')
is_old_enough = ''         # same as None i.e False
has_license = 0            # 0 (Zero) is False

print('is_old_enough', is_old_enough, bool(is_old_enough))
print('has_license', has_license, bool(has_license))