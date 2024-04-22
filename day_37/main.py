import requests

api_endpoint = 'https://pixe.la/v1/users'

params= {
    "token": "naamaavitsur",
    "username": "naamaavitsur",
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

response = requests.post(url=api_endpoint, json=params)
print(response.text)