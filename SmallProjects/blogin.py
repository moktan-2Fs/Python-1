class Login:
  def __init__(self,email,id):
    self.email = email
    self.id = id
  def is_valid_email(self):
    return '@' in self.email and self.email.endswith('.com')
# person = Login("sagarmoktan",'9868343434')
# print(person.is_valid_email())
# print(person.is_valid_number())