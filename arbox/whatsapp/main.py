import requests
import json

url = 'https://graph.facebook.com/v19.0/329694100227112/messages'
headers = {
    'Authorization': 'Bearer EAAGYfgSjZBMYBO4EuNmHb2tTwsZAkitkZAcU6ISTar5O3GvyOdJq4QdaVNUZBjUSNaZCmtcW3gnIAPHyMI6ZC42yMrbVDIpFDeNWZBz3L6ExepOcHryBs6TsDR5Lc1xKoQCWgl7xGHLxAR9UYN4pYBUU7hNA281BIVHh9wuoxqmA7TBdRIDHzr5nKo9eBa6kVSKNfBfBoIbizjIOKiOLwJ0je3jOCkh',
    'Content-Type': 'application/json'
}
data = {
    "messaging_product": "whatsapp",
    "to": "972547833192",
    "type": "template",
    "template": {
        "name": "hello_world",
        "language": {
            "code": "en_US"
        }
    }
}

response = requests.post(url, headers=headers, data=json.dumps(data))

print(response.status_code)
print(response.json())