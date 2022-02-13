import requests
import json

url = "https://secure.paytabs.com/payment/token"

payload = "{\n    \"profile_id\": 59313 ,\n    \"token\": \"2C4650BC67A3E833C6B791FB608779B8\"\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

