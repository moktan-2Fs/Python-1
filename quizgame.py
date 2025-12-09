#game simple

#quiz in python
# questions = ("How many elements are there in periodic table?: ",
#              "Which animal lays the largest eggs?: ",
#              "How many bones are there in the human body?: ",
#              "Which planet in the solar system is the hottest? ")
# options = (
#   ("A. 113","B.118","C. 116","D. 117"),
#   ("A. Ostrich","B. Kiwi","C. Penguin","D. Golden Eagle"),
#   ("A. 200","B.210","C. 206 ","D. 300"),
#   ("A. Earth","B. Mars","C. Venus ","D. Jupiter"))
# answers = ("C","A","C","C")
# score = 0
# i = 1
# for queston in questions:
#   print(f"\n{i}. {queston}")
#   j = 1
#   k = 0
#   for option in options:
#     j += 1
#     print(option[k], end= " ")
#     k += 1
#     # print(f"{j}. {option}")
#     print()
#   ans = input("Enter the answer: ")
#   for x in answers:
#     if ans.lower() == x.lower():
#       score += 1
#     else:
#       continue
#   i += 1
# print(score)


#bro solved this 
# questions = ("How many elements are there in periodic table?: ",
#              "Which animal lays the largest eggs?: ",
#              "How many bones are there in the human body?: ",
#              "Which planet in the solar system is the hottest? ")
# options = (
#   ("A. 113","B. 118","C. 116","D. 117"),
#   ("A. Ostrich","B. Kiwi","C. Penguin","D. Golden Eagle"),
#   ("A. 200","B.210","C. 206 ","D. 300"),
#   ("A. Earth","B. Mars","C. Venus ","D. Jupiter"))
# answers = ("C","A","C","C")
# score = 0
# i = 1
# qstn_num = 0
# for queston in questions:
#   print(f"\n{i}. {queston}")
#   for option in options[qstn_num]:
#     print(option, end= " ")
#     print()
#   ans = input("Enter the answer: ").upper()
#   i += 1
#   if ans == answers[qstn_num]:
#     score += 1
#   qstn_num += 1
# print("You scored: ",score," in the test.")
