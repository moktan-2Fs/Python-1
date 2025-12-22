# num_stop = int(input("Enter the stopping number: "))
# for i in range(2,num_stop):
#   count = 0
#   for j in range(2,i):
#     if i % j == 0:
#       count += 1
#   if count == 1:
#     k = i * 2
#     if k % 2 == 0:
#       print(k)

num = int(input("Enter any number: "))
i = 2
prime_list = []
while i <= num:
  j = 2
  count = 0
  while j <= i:
    if i % j == 0:
      count += 1
    j += 1
  if count == 1:
    prime_list.append(i)
    # print(i)
  i += 1
print(prime_list)

for prime in prime_list:
  for i in prime_list:
    if prime + i == num:
      print(f"{prime}+{i} = {num}")