import os.path
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from bs4 import BeautifulSoup


def connectgmailApi():
    # If modifying these scopes, delete the file token.json.
    scopes = ['https://www.googleapis.com/auth/gmail.readonly']
    token = 'C:/Users/asif.rouf/PycharmProjects/pythonProject/AX_Admin_portal/Test/utils/google-api-token.json'
    credential = 'C:/Users/asif.rouf/PycharmProjects/pythonProject/AX_Admin_portal/Test/utils/google-api-credentials.json'
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, scopes)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(credential, scopes)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        # with open('token.json', 'w') as token:
        #     token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)
    return service


def getlastestmail(service):
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    latestemail = messages[0]
    # print(latestemail)
    return latestemail


def getemailbody(service, latestemail):
    msg = service.users().messages().get(userId='me', id=latestemail['id']).execute()

    try:
        msgsnippet = msg['snippet']
        # print(msgsnippet)
        # Get value of 'payload' from dictionary 'txt'
        payload = msg['payload']
        # print(payload)
        headers = payload['headers']
        subject = ''
        sender = ''

        # Look for Subject and Sender Email in the headers
        for d in headers:
            if d['name'] == 'Subject':
                subject = d['value']
            if d['name'] == 'From':
                sender = d['value']
        # The Body of the message is in Encrypted format. So, we have to decode it.
        # Get the data and decode it with base 64 decoder.
        parts = payload.get('parts')[0]
        data = parts['body']['data']
        data = data.replace("-", "+").replace("_", "/")
        decoded_data = base64.b64decode(data)

        # Now, the data obtained is in lxml. So, we will parse
        # it with BeautifulSoup library
        soup = BeautifulSoup(decoded_data, "lxml")
        body = soup.body()

        # Printing the subject, sender's email and message
        # print("Subject: ", subject)
        # print("From: ", sender)
        # print("Message: ", body)
        link = soup.find('a', href=True)
        # print(link['href'])
        return subject, msgsnippet, link
    except:
        print('Error reading sign up page url from gmail')


