import requests





r = requests.get('http://127.0.0.1:8000?q=test+search')

print(r.text)