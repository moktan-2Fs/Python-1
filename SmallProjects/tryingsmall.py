name_list = ["sagar", 'tamang','lal']
names = ""
for name in name_list:
  names = names  + name + " "
with open("file.txt", "w+") as file:
  file.write(names)