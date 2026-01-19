def length(upass):
  return len(upass)

def numbers(upass):
  count = 0
  for up in upass:
    if up.isdigit():
      count += 1
  return count 

def uniq_chars(upass):
  count = 0
  uqchars = '*&#@!$%^'
  for up in upass:
    if up in uqchars:
      count += 1
  return count 

def upper_count(upass):
  count = 0 
  for i in upass:
    if i.isupper():
      count += 1
  return count

def final_count(upass):
  lenpass = length(upass)
  num_count = numbers(upass)
  unique_count = uniq_chars(upass)
  upper_case = upper_count(upass)
  if lenpass > 4 and num_count >= 2 and unique_count > 1 and upper_case > 1:
    return 1
  else:
    return 0
