import requests as rq

params = {
  "name": "Moktan",
  'age': 23,
  'status': "single"
}

response = rq.get("https://httpbin.org/get", params=params)
print(response.url)

print(response.text) # give the full content of the response 

res_json = response.json()
print(res_json) # gives the content in the form of dictionary 
del res_json['origin']

print()

print(res_json)

print(response.status_code)
