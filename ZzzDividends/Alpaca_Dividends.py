from Objects import Clients

client = Clients.myRealClient()

var = client.polygon.dividends('AAPL')
# var = client.polygon.dividends#('AAPL')

# print(var)
# for v  in var.__iter__():
    # print(v)
# print(var.get('paymentDate'))

import requests

url = 'https://dataondemand.nasdaq.com/api/v1/authenticate'

payload = {'client_key':'__key__', 'client_secret':'__secret__'}
headers = {'Content-Type': 'application/json'}

response = requests.request('POST', url, json=payload, headers=headers)

print(response.text)