import os
sqlUsername = os.getenv('MYSQL_USERNAME')
# sqlUsername = os.environ['MYSQL_USERNAME']
sqlPassword = os.getenv('MYSQL_USERPASSWORD')
sshPrivatekey_path = os.getenv('SSH_PRIVATEKEY_PATH')

# print(sqlUsername, sqlPassword, sshPrivatekey_path)