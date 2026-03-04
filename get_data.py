import requests
request=requests.get("http://127.0.0.1:8000/")
data=request.json()
print(data)
