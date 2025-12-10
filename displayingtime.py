import time 
i = 0
j = 0
k = 0
min = int(input("Enter the minutes: "))
sec = min*60
while  i<min:
  j = 0
  while j<60: 
    time.sleep(1)
    if i > 9:
        print(f"{i}:{j+1}")
    elif j == 59:
       print(f"{k}{i+1}:00")
    elif j < 9:
       print(f"0{i}:0{j+1}")
    else:
        print(f"{k}{i}:{j+1}")
    j += 1
  i += 1