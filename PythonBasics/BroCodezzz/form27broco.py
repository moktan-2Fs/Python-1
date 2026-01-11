import random 
import time
# print(help(random)) 
# low = 1
# high = 50
# optins = ("rock","paper","scissors")
# cards = ["2","k","q","A"]
# random.shuffle(cards)
# print(cards)
# option = random.choice(optins)
# print(option)
# flonu = random.random()
# print(flonu)
# num = random.randint(low,high)
# print(num)

#guessing number game
# num = random.randint(1,50)
# i = 0
# while True:
#   user_num = int(input("Guess a number between 1 to 50: "))
#   i += 1
#   if user_num > num:
#     print(f"It's lower guess between {1} and {user_num}: ")
#   elif user_num < num:
#     print(f"It's higher guess between {user_num} and {50}: ")
#   else:
#     break 
# print(f"You have sucessfully guessed the number {num} in {i} attempts.") 

#rock sissor and  paper game 
# print("\n-----Rock Scissors Paper Game-----")
# options = ("rock","paper","scissors")
# mylo = True 
# while mylo:
#   comp_choice = random.choice(options)
#   user_choice = None 
#   print()
#   for opt in options:
#     print(opt, end= "  ")
#   print()
#   while user_choice not in options:
#     user_choice = input("\nEnter your choice: ").lower().strip()
#   time.sleep(1)
#   print("\nYour choice:","      ",user_choice)
#   print("Computers choice:"," ",comp_choice)
#   if user_choice == comp_choice:
#     print("Draw\n")
#   elif user_choice == "rock" and comp_choice == "paper" or user_choice == "scissors" and comp_choice == "rock" or user_choice == "paper" and comp_choice == "scissors":
#     print("you loose\n")
#   else:
#     print("you win\n")
#   if not input("\"H\" to continue else quits: ").lower().strip() == "h":
#     mylo = False
# print("\n-----Thanks For Playing-----\n")

#30 tutorial bro
# print(" \u25CF \u2500 \u2510 \u250C \u2502 \u2514 \u2518")
#  ● ─ ┐ ┌ │ └ ┘
#  "┌────────┐"
#  "│        │"
#  "│   ●    │"
#  "│        │"
#  "└────────┘"
# dice_art ={
#  1: ( "┌────────┐",
#       "│        │",
#       "│   ●    │",
#       "│        │",
#       "└────────┘"),
# 2:  ( "┌────────┐",
#       "│ ●      │",
#       "│        │",
#       "│      ● │",
#       "└────────┘"),
# 3: (  "┌────────┐",
#       "│  ●     │",
#       "│    ●   │",
#       "│      ● │",
#       "└────────┘"),
# 4: (  "┌────────┐",
#       "│  ●   ● │",
#       "│        │",
#       "│  ●   ● │",
#       "└────────┘"),
# 5: (  "┌────────┐",
#       "│ ●    ● │",
#       "│   ●    │",
#       "│ ●    ● │",
#       "└────────┘"),
# 6: (  "┌────────┐",
#       "│ ●    ● │",
#       "│ ●    ● │",
#       "│ ●    ● │",
#       "└────────┘")
# }
# dice = []
# total = 0
# num_of_dice = int(input("How many dice? "))
# for die in range(num_of_dice):
#   dice.append(random.randint(1,6))

# for die in range(num_of_dice):
#   for line in dice_art.get(dice[die]):
#     print(line)

# for die in dice:
#   total += die
# print(f"total: {total}")
 

#encription program 
# import string 
# # chars = "01"
# chars = " " + string.punctuation + string.digits + string.ascii_letters 
# chars = list(chars) #changing the type of the chars from string to list
# key = chars.copy() 
# random.shuffle(key)
# # print(key)
# # print(chars)
# plain_text = input("enter a message: ")
# cipher_text = ""
# for letter in plain_text:
#   index = chars.index(letter)
#   cipher_text += key[index]
# print("cipher text: ", cipher_text)
# print("original text: ", plain_text)

# cipher_text = input("enter a message: ")
# plain_text = ""
# for letter in cipher_text:
#   index = key.index(letter)
#   plain_text += chars[index]
# print("cipher text: ", cipher_text)
# print("original text: ", plain_text)
# # for cha in chars:
# #   print(cha, end="--")
# # for ke in key:
# #   print(ke,end= "__") 

#functions = A block of reusable code loaced inside () after the function name to invoke it 
# names = [("sagar","raj","rohan","kumar","sanjiv"),("tamang","moktan","shah","moktan","yadav")]
# print(names[1][2])
# for nam , cas in names:
#   print(name)
# def moktan(nam,cast):
#   print(nam,cast,end=" ")
#   print()
# for i in range(len(names[0])):
#   nam = names[0][i]
#   cast = names[1][i]
#   moktan(nam,cast)
# print("sagar moktan \n" * 5,end= "")
# def display_invoice(username, amount, due_date):
#   print(f"hello {username}")
#   print(f"your bill of Rs.{amount} is due: {due_date}")
# display_invoice("Sagar Tamang",5000,"2025-10-05")
# display_invoice("Roshan K.C.",3000,"2025-10-25")

#return = statement used to end a function and send a result back to caller

# def add_num(a,b): return float(a + b)
# print(add_num(1000,1000))
# print("str" + "ing")
# st = "moktan"
# print(st.capitalize()) #capitalize makes the first letter capital and lower cases the other letters in the string 

#default argument = A defult argument value for certain parameters default is used when 
                    # that argument is omitted make your functions more flexible, reduces # of arguments 
                    # 1. Positional, 2. DEFAULT, 3. keyword, 4. arbitrary
  
# def net_price(list_price, disc=0 , tax=5.5):
#   return list_price * (1-disc) * (1+tax)
# print(net_price(500))
# print(net_price(500,0.9))

# import time 
# def count(start,end):
#   for x in range(start,end):
#     time.sleep(0.5)
#     print("hello world")
#   print("Thank You")
# cou = int(input("Enter the starting of the number: "))
# en = int(input("Enter the end of the number: "))
# count(cou,en) 