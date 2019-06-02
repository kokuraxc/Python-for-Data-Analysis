empty_dict = {}
print(empty_dict)

d1 = {

    'a': 'some value',
    'b': [1, 2, 3, 4, 5,]
}
d1[7] = 'an integer'
print(d1) 
d1

d1['b']

'b' in d1

d1[5] = 'some value'
d1
d1['dummy'] = 'another value'
d1

del d1[5]
d1
d1.keys()
d1.values()
list(d1.keys())

list(d1.values())

d1.update({'b': 'foo', 'c': 12})
d1

mapping = {}
key_list = [1, 2, 3, 4, 'x']
value_list = ['xxx', 'jekl', 'hell', [12, 3], 11]
for key, value in zip(key_list, value_list):
    mapping[key] = value

mapping
mapping = {}
for x in mapping:
    del mapping[x]

mapping.clear()
mapping = dict(zip(range(5), reversed(range(5))))
mapping

mapping = dict(zip(key_list, value_list))
mapping

value = mapping.get(1, 'hello')
value

words = ['apple', 'bat', 'bar', 'atom', 'book']
by_ltter = {}
for word in words:
    letter = word[0]
    by_ltter.setdefault(letter, []).append(word)
by_ltter

by_ltter.clear()
by_ltter

from collections import defaultdict
by_ltter = defaultdict(list)
for word in words:
    by_ltter[word[0]].append(word)

by_ltter

dict(by_ltter)

