import requests

BASE = " http://192.168.1.40:1337/"
response = requests.get(BASE + "radioData")
print(response.json())