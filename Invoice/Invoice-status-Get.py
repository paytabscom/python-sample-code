import requests
import json

url = "https://secure.paytabs.com/payment/invoice/1487933/status"

payload={}
headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)