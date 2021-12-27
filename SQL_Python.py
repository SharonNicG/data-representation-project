import mysql.connector
import dbconfig as cfg

db = mysql.connector.connect(
	host=cfg.mysql['host'],
	username=cfg.mysql['username'],
	password=cfg.mysql['password'],
	database=cfg.mysql['database']
)

cursor = db.cursor()
sql ="select * from biscuitinfo"


cursor.execute(sql)
result = cursor.fetchall()
for x in result:
	print(x)