print("hello and welcome to calculator..")
print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Division \n 5. Exit")
while True:
    try: 
        user_choi = input("Choice: ")
        if any(cha in user_choi for cha in "12345"):
            break
    except Exception:
        print('there were some error with your input you jackasss.....')
    finally:
        print("try again with proper inputs....")
