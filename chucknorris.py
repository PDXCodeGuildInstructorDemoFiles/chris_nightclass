import requests

payload = {'appid': '23452345'}
r = requests.get('http://api.icndb.com/jokes/random')
data = r.json()
print(r.status_code)
print(data['value']['id'])
print(data['value']['joke'])
