import requests as rq

# params = {
#     "name": 'SagarMoktan', 
#     "age": 22,
#     "gender": "Male"
# }
# url = 'https://httpbin.org/get'
# response = rq.get(url, params= params)
# print(response.status_code)
# print(response.url)

# # print(response.text)
# res_json = response.json()
# print(res_json, type(res_json))
# # del res_json['origin']

# for key, value in res_json.items():
#     print(key, value)
#     print("\n")

# url = "http://127.0.0.1:8000"
# parm = input('PageName: ')
# f_url = url + '/' + parm
# response = rq.get(f_url)

# print(response.status_code)
# data = response.json()

# print(data )

# post


payload = {
    "name": 'SagarMoktan', 
    "age": 22,
    "gender": "Male"
}
# url = 'https://httpbin.org/status/554'
# response = rq.get(url)

# if response.status_code == rq.codes.not_found:
#   print("Not found sorry.....")

# print(response.status_code)
# print(response.url)
headers = {
  'User-Agent': 'SagarMoktaan',
  'Accept': 'image/webp'
}

url = 'https://httpbin.org/image'
# ress =  rq.get(url, headers= headers)
# print(ress, ress.status_code, ress.text, ress.json(), end= "\n") 
reque = rq.get(url, headers= headers)
with open('./myimage.webp','wb') as f:
  f.write(reque.content)

