import os
import requests
import json
#
token = os.getenv("TOKEN_FACEBOOK")
token_forever = os.getenv("FACEBOOK_FOREVER")

import requests
import json


def send_template():
    url = 'https://graph.facebook.com/v20.0/317183528149149/messages'
    headers = {
        'Authorization': f'Bearer {token_forever}',
        'Content-Type': 'application/json'
    }

    data = {
        "messaging_product": "whatsapp",
        "to": "+972547833192",
        "type": "template",
        "template": {
            "name": "new",
            "language": {
                "code": "en_US"
            }
        }
    }



    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print("Success!")
        print(response.json())  # Print the JSON response
    else:
        print(f"Failed with status code: {response.status_code}")
        print(response.text)  # Print the error message



def send_text():
    url = 'https://graph.facebook.com/v20.0/317183528149149/messages'
    headers = {
        'Content-Type': 'application/json',
        'Authorization': f'Bearer {token_forever}'
    }

    data = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": "+972547833192",
        "type": "text",
        "text": {
            "preview_url": True,
            "body": "היי שי מה המצב אני כותבת לך בטקסט"
        }
    }


    response = requests.post(url, headers=headers, data=json.dumps(data))

    # Check the response
    if response.status_code == 200:
        print("Success!")
        print(response.json())  # Print the JSON response
    else:
        print(f"Failed with status code: {response.status_code}")
        print(response.text)  # Print the error message

# send_text()
send_template()