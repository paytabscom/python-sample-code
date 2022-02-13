import requests
import json

url = "https://secure.paytabs.com/payment/invoice/status"

payload = "{\r\n    \"profile_id\": 59313 ,\r\n    \"invoice_id\": 1487933 \r\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)