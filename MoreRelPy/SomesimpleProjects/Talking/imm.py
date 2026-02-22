import easyocr
import torch
# print(torch.version.cuda)
# print(torch.cuda.is_available())
# print(torch.cuda.get_device_name(0))
reader = easyocr.Reader(['en'], gpu= True)
result = reader.readtext('im2.jpeg')

for detection in result:
    print(detection[1])
