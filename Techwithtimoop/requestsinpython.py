import requests as rq

payload = {
  "name": "Moktan",
  'age': 23,
  'status': "single"
}

response = rq.post("https://httpbin.org/post", data=payload)
print(response.url)

print(response.text) # give the full content of the response 

res_json = response.json()
print(res_json) # gives the content in the form of dictionary 
del res_json['origin']

print()

print(res_json)

print(response.status_code)
