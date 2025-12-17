# f =  open("compfile.txt","w")
# f.write("hello from the other side....\n")
# f.write("This is also a file that I wrote from the .write() function.")

# f = open("compfile.txt","r")
# print(f.readline(),end= "")
# print(f.read(6))

# f = open("compfile.txt","r")
# for li in f:
#   print(f.readline())

# f = open("compfile.txt","r+")
# f.write("Writing in r+ mode;....")
# print(f.read())
# # f.write("\nNew line added to the file from the filehandlingcomp.py file")
# print(f.read())
# f.close()

with open("moktan.txt","w+") as file:
  file.write("Hello form the other side.....")
  