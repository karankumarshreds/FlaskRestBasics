import requests 

BASE = "http://localhost:5000"

response = requests.post(BASE + "/people/karan", { "age": 29 })
print(response.json())
