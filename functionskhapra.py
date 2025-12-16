# def to define a function 
# def calc_sum(a,b): return a+b
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
# print(calc_sum(num1,num2))
# print(calc_sum(5,8)+calc_sum(num1,num2))

# def cal_ave(a=1,b=1,c=1):
#   return (a+b+c)/3
# print(cal_ave(5,3))

# def hello():
#   print("hello moktan")
# for i in range(8):
#   hello()

# def mul_2(a=1,b=1):
#     return a*b
# print(mul_2())

# list_1 = ["sagar","kamala","dolakha",6,5,33,3]
# def len_gi(a):
#     for i in a:
#         print(i,end = " ")
#     return len(a)
# len_gi(list_1)

# def factorl(n):
#   fact = 1
#   for i in range(1,n+1):
#     fact *= i
#   print(fact)
# f = int(input("enter the number whichs factorial you want: "))
# factorl(f)

#currency conversion
# rate = 143.5
# neprs = 0
# def convers(a):
#     a /= rate
#     return a 
# neprs = int(input("Enter the amount you want to convert: "))
# usd = convers(neprs)
# print(f"Rs.{neprs} = {usd:.2f}$")

#recursion 
# def show(n):
#     if n == 0: # this is a base case for recursion that
#         return  # stops the recursion and returns the values 
#     print(n)
#     show(n-1)
#     print("prints while returning from basecase")
# show(5)
 
#call stack for understanding recursion 
# def re_fact(n):
#     if n == 0 or n == 1 :
#         return 1
#     return n*re_fact(n-1)
 
