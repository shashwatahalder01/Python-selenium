

import requests
import json
import pytest
from requests.exceptions import HTTPError

# url = "https://dev2.augmedix.com:50000/token?grantType=password&idp=com.augmedix.legacy"
# payload = "{\"username\": \"jorge.zendejas_admin1@augmedix.com\", \"password\": \"Admin123$12\", \"userType\": \"admin\"}"
url = "https://staging-api.augmedix.com:50000/token?grantType=password&idp=com.augmedix.legacy"
payload = "{\"username\": \"stage_gd_scribe2@augmedix.com \", \"password\": \"1Augmedix\", \"userType\": \"scribe\"}"
headers = {
    'Content-Type': 'application/json'}

try:
    response = requests.request("POST", url, headers=headers, data=payload)
    # print(response.text)
    response.raise_for_status()
    body = json.loads(response.text)
    token = body['token']
    print("TOKEN :", token)

except HTTPError as http_err:
    pytest.fail()
    print(f'HTTP error occurred: {http_err}')
except Exception as err:
    pytest.fail()
    print(f'Other error occurred: {err}')
else:
    print('Success!')
    # print("Response:", response.status_code)

# eyJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20uYXVnbWVkaXgiLCJleHAiOjE2MjM4NjgzMzgsInVpZCI6MzIxNCwicmxzIjpbIlNDUklCRSJdfQ.Mp8c8zcEMKd2zb1orKopotOx9UEzJAKxu41wzrCcfEA