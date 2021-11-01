import pymysql
import paramiko
from sshtunnel import SSHTunnelForwarder
from data.Database.readenv import sql_username, sql_password, ssh_privatekey_path
sql_hostname = "augmedix-staging.ckxiwwu7ushh.us-east-2.rds.amazonaws.com"
sql_main_database = "augmedix"
sql_port = 3306
ssh_host = '18.218.111.138'
ssh_user = 'ec2-user'
ssh_port = 22
ssh_privatekey = paramiko.RSAKey.from_private_key_file(ssh_privatekey_path)

tunnel = SSHTunnelForwarder(
         (ssh_host, ssh_port),
         ssh_username=ssh_user,
         ssh_pkey=ssh_privatekey,
         remote_bind_address=(sql_hostname, sql_port))
tunnel.start()
db = pymysql.connect(
    # host='127.0.0.1',
    user=sql_username,
    passwd=sql_password,
    db=sql_main_database,
    port=tunnel.local_bind_port,
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor
)

cursor = db.cursor()
