import requests

response = requests.get("https://api.npoint.io/33acc64b78645f6c2fd3")
print(response.json())
