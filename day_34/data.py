import requests
import html
parameters = {
    "amount": 10,
    "category": 11,
    "type": "boolean"
}
response = requests.get("https://opentdb.com/api.php", params=parameters)
response.raise_for_status()
data = response.json()['results']
question_data = [{'question': html.unescape(item['question']), 'correct_answer': html.unescape(item['correct_answer'])} for item in data]



