import requests
res = requests.get("http://localhost:2137/").text
print(res)