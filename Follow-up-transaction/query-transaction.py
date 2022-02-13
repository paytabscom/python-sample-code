import re
import requests
import json

url = "https://secure.paytabs.com/payment/query"

payload = "{\n    \"profile_id\": 59313 ,\n    \"tran_ref\": \"TST2131800438795\"\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)