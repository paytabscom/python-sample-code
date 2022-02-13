import requests
import json

url = "https://secure.paytabs.com/payment/token/delete"

payload = "{\n    \"profile_id\": 59313 ,\n    \"token\": \"2C4652BE67A3E534C6B790FE64857FBA\"\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

