import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import email
import base64
from bs4 import BeautifulSoup
from datetime import datetime

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']


def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    token = 'C:/Users/asif.rouf/PycharmProjects/pythonProject/AX_Admin_portal/Test/utils/google-api-token.json'
    credential = 'C:/Users/asif.rouf/PycharmProjects/pythonProject/AX_Admin_portal/Test/utils/google-api-credentials.json'
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(token):
        creds = Credentials.from_authorized_user_file(token, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                credential, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        # with open('token.json', 'w') as token:
        #     token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # # Call the Gmail API
    # results = service.users().labels().list(userId='me').execute()
    # labels = results.get('labels', [])
    #
    # if not labels:
    #     print('No labels found.')
    # else:
    #     print('Labels:')
    #     for label in labels:
    #         print(label['name'])

    # Call the Gmail API to fetch INBOX
    results = service.users().messages().list(userId='me', labelIds=['INBOX']).execute()
    messages = results.get('messages', [])
    # message1 = messages[0]
    # print(message1)
    message1 = {'id': '17a5ca5f5f4bd0aa', 'threadId': '17a5b1bb861b3bc2'}
    message1 = {'id': '17a5cbc54c546465', 'threadId': '17a5b1bb861b3bc2'}

    # message1 = {'id': '17a5b852afe04a52', 'threadId': '17a50c997c059e68'}
    print(messages)
    print(message1)

    if not messages:
        print("No messages found.")
    else:
        print("Message snippets:")
    #     for message in messages:
    #         msg = service.users().messages().get(userId='me', id=message['id']).execute()
    #         print(messages)
    #         print(msg['snippet'])

        # msg = service.users().messages().get(userId='me', id=message1['id']).execute()
        # print(msg['snippet'])
        ###############################
        msg = service.users().messages().get(userId='me', id=message1['id'], format='raw').execute()
        msg_str = base64.urlsafe_b64decode(msg['raw'].encode('ASCII'))
        mime_msg = email.message_from_bytes(msg_str)
        print(msg['snippet'])
        print(mime_msg)
        print(mime_msg['Date'])
        print(mime_msg['From'])
        print(mime_msg['To'])
        print(mime_msg['Subject'])
        #
        # print(datetime.utcnow())

        ######################################################
        # msg = service.users().messages().get(userId='me', id=message1['id'], format='full').execute()
        # # parts can be the message body, or attachments
        # payload = msg['payload']
        # headers = payload.get("headers")
        # parts = payload.get("parts")
        # # print(payload)
        # # print(parts)
        # # print(headers)
        # for header in headers:
        #     print(header['name'])
        #     print(header['value'])
        #
        ######################################################
        msg = service.users().messages().get(userId='me', id=message1['id']).execute()

        # Use try-except to avoid any Errors
        try:
            # Get value of 'payload' from dictionary 'txt'
            payload = msg['payload']
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
            print("Subject: ", subject)
            print("From: ", sender)
            print("Message: ", body)
            # for link in soup.find_all('a', href=True):
            #     print(link['href'])
            link = soup.find('a', href=True)
            print(link['href'])
        except:
            pass



if __name__ == '__main__':
    main()
