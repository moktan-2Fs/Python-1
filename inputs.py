import math
# students_count = 100
# collg_name = "Kist College"
# is_purbanchal = True
# print(f"Is {collg_name} a verified in Nepal:{is_purbanchal}")
# #triple quotes are used to format a long string it also takes the line brakings in
# message = """ hello thare alfjla
# af lakdfja
# amsjflas kasf
# asfj alsfa
# sf aslkfas
# fflak
# """
# print(message)
# #len() funct is used for getting the total characters in the string passed as arguments
# print(len(message))
# print(collg_name[0])
# print(collg_name[-1])
# print(collg_name[:4])
# print(collg_name[:])
# course='Python "Programming"'
# course = "python \nProgramming"#here \is a escape character that doesnt code the character behind it
# # print(course)
# # some of the escape sequences in python are \", \', \n(is used for newline) and \\ , the character after backslash are printed without showing errors
# first_name = "Sagar"
# last_name = "Tamang"
# full_name = f"{first_name} {last_name}" #this f"" is a formatted string any thing can be put inside it
# # full_name = first_name + " " + last_name
# print(full_name)

# course = "python programming"
# print(course.find("ng"))
# print(course.replace("g","k"))
# print("po" in course) # 'in' is used for checking the existanc of any character of sequence of characters in the string
# print(course)
# print("swift" not in course)
# x = 1 + 2j
# print(10 + 3)
# print(10 - 3)
# print(10 / 3) # "/" gives you the quotient as it is (may be integer or float)
# print(10 // 3) #"//" gives you the quotient in integer form
# print(10 % 3)
# print(10 ** 3)

# print(round(3.43))  # round roundoffs the float number to integer
# print(abs(-33.5))  # abs returns the absolute value of the number
# print(math.ceil(3.3))  # ceil roundoffs to nearest upper integer value
# print(math.factorial(5))
# print(math.comb(100, 5))
# print(math.tau)
# x = int(input("Enter the number you like:"))
# x += 3
# print(f"The number is {x}")
# print(type(x))

# # ""(empty), 0 , None are the valus that are false if any variable contains it else are true
# print(bool(0))
# print(bool(""))
# print(bool(None))
# print(bool("sagar"))
# print(bool(1))
num= int(input("Enter any number:"))
if num%2 == 0:
    print(num**2)
else:
    print(num**3)
    