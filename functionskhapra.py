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

# currency conversion
# rate = 143.5
# neprs = 0
# def convers(a):
#     a /= rate
#     return a
# neprs = int(input("Enter the amount you want to convert: "))
# usd = convers(neprs)
# print(f"Rs.{neprs} = {usd:.2f}$")

# recursion
# def show(n):
#     if n == 0: # this is a base case for recursion that
#         return  # stops the recursion and returns the values
#     print(n)
#     show(n-1)
#     print("prints while returning from basecase")
# show(5)

# call stack for understanding recursion
# def re_fact(n):
#     if n == 0 or n == 1 :
#         return 1
#     return n*re_fact(n-1)

# f = open("ignofile.txt", "r")

# # reads the first line from the file(only 1st line and rest can be also done in line or as a whole by read())
# data_infile_line1 = f.readline()
# # sending parameters gives the characters in the parameters numbers eg: (5) gives first 5 characters from the file
# data_infile = f.read()
# print(data_infile_line1)
# print(type(data_infile))
# print(data_infile, end="")
# f.close()

# "r" for reading
# "w" for writing
# "x" for new file and open for writing
# "a" for appending to the end of the file if it exists
# "b" binary mode
# "t" text mode(default)
# "+" open a disk file for updationg (reading and writing )

# writing to a file
# f = open("ignofile.txt", "a")
# f.write('Also I love girls with certain behaviours... \n')
# print(f)
# f.close()

# f = open("ignofile.txt", "r")
# print(f.read())
# f.close()






# lambda x, y: x+y
# lambda(5,6)


# freecodecamp
# my_range_var = range(5)
# print(my_range_var)
# print(isinstance("hello world",str))

# user_name: str = 'Moktan Sagar'
# print(user_name[1:9:3])