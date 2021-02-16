import requests 

BASE = "http://localhost:5000"

response = requests.get(BASE + "/home/4")
print(response.json())



