import requests
res = requests.get('https://www.orangepage.net')
print(res.text)