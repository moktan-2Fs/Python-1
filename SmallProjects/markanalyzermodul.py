import random as rd
names = ""
marks = ""
subjs = ""
bool_value = True
count = 0
name_list = []
roll_list = []
sub_list = []
marks_list = []
no_of_students = int(input("Enter the no. of students: "))
no_of_subjs = int(input("Enter the no. of subjects: "))
print("Enter the subject name: ")
for j in range(no_of_subjs):
    subj = input(f"{j+1}: ").capitalize()
    sub_list.append(subj)
sub_list.sort()
# print(sub_list)
while bool_value:
    for i in range(no_of_students):
        name = input(f"Enter the name of student: ").title()
        roll = input(f"Enter the roll no. of {name}: ")
        name_list.append(name)
        roll_list.append(roll)
        print("Enter the marks obtained on: ")
        for j in sub_list:
            mark = (input(f"{j}:"))
            marks_list.append(mark)
        count = 1
    with open("records.txt", "w+") as file:
        for name in name_list:
            names = names + name + ", "
        file.write("Names: ")
        file.write(names)
        for subs in sub_list:
            subjs = subjs + subs + ", "
        file.write("\nSubjects: ")
        file.write(subjs)
        i = 0
        for mar in marks_list:
            if i == no_of_subjs:
                marks += "   "
            marks = marks + mar + ","
            i = i + 1
        file.write("\nMarks Obtained: ")
        file.write(marks)
    if count == 1:
        print("loop ends now")
        bool_value = False
