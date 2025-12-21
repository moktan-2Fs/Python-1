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
num = 20 
i = 2
prime = 0
while i <= 20:
  j = 2
  count = 0
  while j <= i :
    if i % j == 0:
      count += 1
    j += 1
  if count == 1:
    # print(i)
    k = i * 2
    if k % 2 == 0:
      print(f"{i}+{i} = {k}")
    prime += 1
  i += 1 