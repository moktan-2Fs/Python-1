
# num = [3,2,3,2,6]
# squared = list(map(lambda x: x**2,num))
# print(squared,type(squared))

# map() -> modifies every item
# filter() -> removes some items
# def add(x, y): return x**y


# print(add(2, 5))


# def is_odd(num): return num % 2 != 0


# print(is_odd(5))
# map applies a function to every item in a list: syntax: x = list(map(function,iterable)), list because map returns a map object
# num = [1, 2, 3, 4, 5, 6, 7, 8]
# result = list(map(lambda x: x**2, num))
# print(result)

# filter= keep only some, syntax = filter(function,iterable), function must return boolean value

# evens = list(filter(lambda x: x % 2 == 0, num))
# print(evens, 'type:', type(evens))
# lambda checks
# 1 -> False, throw
# 2 -> True, Kedp
# 3 -> false, throw
# and so on


# practice qstns
# nums = [2, 5, 8, 11, 14]
# print(nums)
# doubled = list(map(lambda x: x*2, nums))
# filterd_greater_num = list(filter(lambda x: x > 15, doubled))
# print(doubled)
# print(filterd_greater_num)

# names = ['ram', 'sagar', 'ai', 'python', 'go']
# print(names)
# filtered_names = list(filter(lambda name: len(name) > 3, names))
# upper_names = list(map(lambda name: name.upper(), filtered_names))
# print(filtered_names)
# print(upper_names)

# numms = [1, 2, 3, 4, 5, 6]
# print(numms)
# even_fil = list(filter(lambda num: num % 2 == 0, numms))
# squared = list(map(lambda num: num**2, even_fil))
# print(even_fil)
# print(squared)

# nums = [1,2,3,4,5]
# result = list(
#     map(lambda x: x+1,
#     filter(lambda x: x%2 != 0,nums))
# )
# print(result)

# names = [
#     'Sagar',
#     'Rohan',
#     'Roshan',
#     'Moktan',
#     'json'
# ]
# result = list(
#     filter(lambda name: 'S' in name ,
#         map(lambda name: name.upper(),names))
# )
# print(result)


# sorted -> by using key as lambda

num = [5, 3, 2, 5, 6, 7, 7, 4, 9]
print(sorted(num))
names = [
    'Sagar',
    'Rohan',
    'Roshan',
    'Moktan',
    'json'
]
# key is a function on which basis you want to sort your list in
result = sorted(names, key=lambda x: x[2])
print(result)


dirct = {
    'name': "Moktan",
    'age': 20,
    ' location': 'Kathmandy'
}
mapped_dict = dict(map(lambda item:  (item[0], item[1]), dirct.items()))
print(mapped_dict)
