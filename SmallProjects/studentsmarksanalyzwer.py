class student():
  def __init__(self, s_name, s_roll, s_marks):
    self.name = s_name
    self.roll = s_roll
    self.list_1 = s_marks

while True:
  # no_of_stu = int(input("Enter the no. of students you want to add: "))
  no_of_subj = int(input("Enter the no. of subjects: "))
  stu_subj_list = []
  stu_marks_list = []
  # stud_name = input("Enter the students name: ")
  # stud_roll = int(input("Enter the students roll no. : "))
  for i in range(no_of_subj):
    num = input(f"Enter subject no.[{i+1}] name: ")
    stu_subj_list.append(num)
  # print("Enter the marks obtained in:\n")
  # for i in range(0,no_of_subj-1):
  #   mark = int(input(f"{stu_subj_list[i]}"))
  #   stu_marks_list.append(mark)
  # # for i in range(0,no_of_stu):
  #   stu[i] = student(stud_name,stud_roll,s_marks)

# num = 5
# for i in range(num):sadf
#   print(i)