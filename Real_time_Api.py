import requests
url = 'http://api.airvisual.com/v2/nearest_city?key=f7316a56-f7eb-4c55-9b8e-af9877f75d6a'
payload = {}
files = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.text.encode('utf8'))
