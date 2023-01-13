import requests

response = requests.get('https://opentdb.com/api.php?amount=10&type=boolean')
response.raise_for_status()
data = response.json()
print(data['results'])

question_data = data['results']