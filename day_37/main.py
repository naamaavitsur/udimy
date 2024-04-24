import requests
import datetime

api_endpoint = 'https://pixe.la/v1/users'
user_name = "naamaavitsur"
token = "naamaavitsur"
graph_id = "na98765432"
params= {
    "token": token,
    "username": user_name,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

# response = requests.post(url=api_endpoint, json=params)
# print(response.text)


graph_endpoint = f"{api_endpoint}/{user_name}/graphs"

headers = {
    "X-USER-TOKEN": token

}

body = {
    "id": graph_id,
    "name": "number_of_days",
    "unit": "days",
    "type": "int",
    "color": "ajisai"

}

# graph_response = requests.post(url=graph_endpoint, json=body, headers=headers)
# print(graph_response.text)
date = datetime.date.today().strftime("%Y%m%d")
print(date)
api_date = f"{graph_endpoint}/{graph_id}"
body_graph= {
    "date": date,
    "quantity": "1",

}

# graph_update_response = requests.post(url=api_date, json=body_graph, headers=headers)
# print(graph_update_response.text)

update_date_api = f"{api_date}/{date}"
data_update = {
    "quantity": "3"
}
# upate_response = requests.put(url=update_date_api, json=data_update, headers=headers)
# print(upate_response.text)

delete_response = requests.delete(url=update_date_api, headers=headers)
print(delete_response.text)

