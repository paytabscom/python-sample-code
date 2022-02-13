import requests
import json

url = "https://secure.paytabs.com/payment/request"

payload = "{\n    \"profile_id\": 59313 ,\n    \"tran_type\": \"sale\",\n    \"tran_class\": \"ecom\",\n    \"cart_id\": \"cart_22222\",\n    \"cart_currency\": \"AED\",\n    \"cart_amount\": 12.3,\n    \"cart_description\": \"Description of the items/services\",\n    \"paypage_lang\": \"en\",\n    \"customer_details\": {\n        \"name\": \"first last\",\n        \"email\": \"email@domain.com\",\n        \"phone\": \"0522222222\",\n        \"street1\": \"address street\",\n        \"city\": \"dubai\",\n        \"state\": \"du\",\n        \"country\": \"AE\",\n        \"zip\": \"12345\"\n    },\n    \"shipping_details\": {\n        \"name\": \"name1 last1\",\n        \"email\": \"email1@domain.com\",\n        \"phone\": \"971555555555\",\n        \"street1\": \"street2\",\n        \"city\": \"dubai\",\n        \"state\": \"dubai\",\n        \"country\": \"AE\",\n        \"zip\": \"54321\"\n    },\n    \"callback\": \"\",\n    \"return\": \"\",\n    \"donation_mode\":true,\n    \"cart_min\":5,\n    \"cart_max\":10\n}"

headers = {'authorization': 'S6JN9NWBW9-JBD9GRNRH2-DHD9MGMHRR','Content-Type': 'application/json'}

response = requests.request("POST", url, headers=headers, data=payload)

json_object = json.loads(response.text)

print("PayTabs Url is " + json_object["redirect_url"])