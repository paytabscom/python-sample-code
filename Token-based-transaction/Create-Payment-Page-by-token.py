import requests
import json

url = "https://secure.paytabs.com/payment/request"

payload = "{\n    \"profile_id\": 59313 ,\n    \"tran_type\": \"sale\",\n    \"tran_class\": \"recurring\",\n    \"cart_id\": \"cart_55555\",\n    \"cart_currency\": \"AED\",\n    \"cart_amount\": 100,\n    \"cart_description\": \"Description of the items/services\",\n    \"token\": \"2C4651BE67A3E530C6B791F560837DB1\",\n    \"tran_ref\": \"TST2105900091509\",\n    \"hide_shipping\": true,\n    \"callback\": \"\",\n    \"return\": \"\"\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

json_object = json.loads(response.text)

print("PayTabs Url is " + json_object["redirect_url"])
