import requests

url = 'https://notify-api.line.me/api/notify'
token = 'THIS IS YOUR LINE API TOKEN'
headers = {'content-type': 'application/x-www-form-urlencoded', 'Authorization': 'Bearer ' + token}
message = 'This the test message.'
r = requests.post(url, headers=headers , data = {'message':message})
print(r.text)