import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), ".."))

from Utils.get_token_dg import token

BEARER_TOKEN = 'Bearer ' + str(token)
headers = {'Authorization': BEARER_TOKEN}

BEARER_TOKEN_FALES = "False Token"
headers_wrong = {'Authorization': BEARER_TOKEN_FALES}

headersPost = {'Authorization': BEARER_TOKEN, 'Content-Type': 'application/json'}

headersPostWrong = {'Authorization': BEARER_TOKEN_FALES, 'Content-Type': 'application/json'}
