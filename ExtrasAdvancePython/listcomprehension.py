names = ['sagar', 'ram','moktan', 'hari']
# long_names = []
# for name in names:
#   if len(name) > 4:
#     long_names.append(name)

long_names = [name for name in names if len(name) > 2]
print(long_names)

numbers = [1,2,3,4,5,6,7,8,9,10]
squared = [pow(number,2) for number in numbers if number % 2 == 0]
print(squared)

from typing import Generator
data: range = range(10_000)
squared: Generator[int,None,None] = (pow(n,2) for n in data)
print(squared)
print(next(squared))

values: list[int]  = [5,10,15,20,25]