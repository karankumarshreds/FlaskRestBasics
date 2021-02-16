import requests 

BASE = "http://localhost:5000"

response = requests.post(BASE + "/people/karan", { "age": 26 })
print(response.json())



