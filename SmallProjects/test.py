def email1(email):
  fou = False
  for em in email:
    if em == '@':
      fou = True
    else:
      continue
  if email[len(email)-4: len(email)] == ".com" and fou == True:
    print("the email is valid.")

email1("sagarmoktan@gmail.com")
# email = "sagarmoktan@gmail.com"
# print(email[len(email)-4: len(email)])
