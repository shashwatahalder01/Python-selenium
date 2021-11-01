# import required modules
import pymysql

db = pymysql.connect(
  host="stg-rds.cyenjhoy77oj.us-east-1.rds.amazonaws.com",
  user="qa_admin",
  password="3781726879d38cc3",
  database="dev_augmedix",
  charset='utf8mb4',
  cursorclass=pymysql.cursors.DictCursor
)

cursor= db.cursor()