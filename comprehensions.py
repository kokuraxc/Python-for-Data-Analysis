# list comprehension
# [ exp for val in collection if condition]

strings = ['a', 'as', 'bat', 'dove', 'python']
com = [x.upper() for x in strings if len(x) > 2]
print(com)

# set  comprehensions
unique_lengths = {len(x) for x in strings}
print(unique_lengths)

# map function
unique_lengths_map = set(map(len, strings))
print(unique_lengths_map)

# dict comprehensions
loc_mappings = {val:index for index, val in enumerate(strings)}
print(loc_mappings)

# nested list comprehension ( to flatten lists in list)
all_data = [['john', 'emily', 'michael', 'mary', 'steven'],
            ['maria', 'juan', 'javier', 'natalia', 'pilar']]
result = [name for names in all_data for name in names if name.count('e') >= 2]
print(result)

some_tuples = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
flattened = [x for nums in some_tuples for x in nums]
print(flattened)

# a list comprehension inside a list comprehension produces a list of lists
lol = [[x for x in tup] for tup in some_tuples]
print(lol)

# sort a collection
strings = ['foo', 'card', 'bar', 'aaaa', 'abab']
print(strings)
strings.sort(key = lambda x: len(set(list(x))))
print(strings)

# generator function
def squares(n = 10):
    for i in range(1, n+1):
        yield i ** 2

# for x in squares(25):
#     print(x)

# generator expression
gen = (x ** 2 for x in range(100))

print(sum(x ** 2 for x in range(100)))
print(dict((i, i**2) for i in range(5)))