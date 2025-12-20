def length(upass):
  return len(upass)

def numbers(upass):
  count = 0
  nums = '1234567890'
  for i in range(len(upass)):
    for j in range(len(nums)):
      if upass[i] == nums[j]:
        # print('little strong')
        count += 1
  print("No. of numbers:",count)
  return count 

def uniq_chars(upass):
  count = 0
  uqchars = '*&#@!$%^'
  for i in range(len(upass)):
    for j in range(len(uqchars)):
      if upass[i] == uqchars[j]:
        # print('there are unique chars in the password..')
        count += 1
  print("No. of unique characters:",count)
  return count 

def upper_count(upass):
  count = 0 
  for i in upass:
    if i.isupper():
      count += 1
  print("No. of uppercase: ",count)
  return count

def final_count(upass):
  lenpass = length(upass)
  num_count = numbers(upass)
  unique_count = uniq_chars(upass)
  upper_case = upper_count(upass)
  if lenpass > 4 and num_count > 2 and unique_count > 2 and upper_case > 2:
    print("The password is very very strong....")
  elif (lenpass >5 and num_count >2):
    print("the password is strong.")
  else:
    print("The password is not very strong.")
