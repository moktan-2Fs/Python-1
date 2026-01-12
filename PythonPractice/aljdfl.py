import time 
# arr = [2,2,3]
# for ar in arr:
#   ar *= 2
# print(arr,end= "")

# def add_num(num: int):
#   sum = 0
#   if num == 0:
#     print(f"0")
#   elif num == 1:
#     print(f"1")
#   else:
#     for i in range(num+1):
#       sum += i
#   return sum

# usernum = int(input("Enter number: "))
# print(add_num(usernum))





def add_num(num: int):
  sum = 0
  if num == 0:
    print(f"0")
  elif num == 1:
    print(f"1")
  else:
    for i in range(num+1):
      for j in range(1,101):
        print(f"yohoho!!!!!{i}th {j}")


usernum = int(input("Enter number: "))
st_time = time.time()
add_num(usernum)
ed_time = time.time()
print(f"time taken to complete task is {ed_time-st_time}")