import re
import requests
import json

url = "https://secure.paytabs.com/payment/request"

payload = "{\n    \"profile_id\": 59313 ,\n    \"tran_type\": \"capture\",\n    \"tran_class\": \"ecom\",\n    \"cart_id\": \"cart_66666\",\n    \"cart_currency\": \"AED\",\n    \"cart_amount\": 1.3,\n    \"cart_description\": \"Capture reason\",\n    \"tran_ref\": \"TST2204401056370\"\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)