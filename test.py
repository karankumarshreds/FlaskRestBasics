import requests 

BASE = "http://localhost:5000"

response = requests.get(BASE + "/people/karan")
print(response.json())



