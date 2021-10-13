from sys import getsizeof

#Generate list with List Comprehension
list_comp = getsizeof([x*10 for x in range(1000)])

#Generate list with Set Comprehension
set_comp = getsizeof({x*10 for x in range(1000)})

#Generate list with Dictionary Comprehension
dict_comp = getsizeof({x:x*10 for x in range(1000)})

#Generate list with Generator
gen = getsizeof(x*10 for x in range(1000))

print(f'Bytes used')
print(f'List Comprehension: {list_comp}')
print(f'Set Comprehension: {set_comp}')
print(f'Dict Comprehension: {dict_comp}')
print(f'Generator: {gen}')






