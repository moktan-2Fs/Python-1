class Login:
  def __init__(self,email,num):
    self.email = email
    self.num = num
  def is_valid_email(self):
    return '@' in self.email and self.email.endswith('.com')
  def is_valid_number(self):
    return len(self.num) == 10 and self.num[0] == '9' and (self.num[1] in ['8','7'])
# person = Login("sagarmoktan",'9868343434')
# print(person.is_valid_email())
# print(person.is_valid_number())