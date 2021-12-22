import mysql.connector 
import dbconfig as cfg

class BiscuitsDAO:     
	db=""
	def connectToDB(self):
		self.db = mysql.connector.connect(
			host=cfg.mysql['host'],
			username=cfg.mysql['username'],
			password=cfg.mysql['password'],
			database=cfg.mysql['database']
		)
	def __init__(self):
		self.connectToDB()
		
	def getCursor(self):
		if not self.db.is_connected():
			self.connectToDB()
		return self.db.cursor()
		
	def create (self, values):
		cursor = self.getCursor()
		sql="insert into biscuitinfo (Biscuit_Name, Biscuit_Flavour, Biscuit_Size) values (%s, %s, %s, %s)"
		cursor.execute(sql, values)

		self.db.commit()
		lastRowId=cursor.lastrowid
		cursor.close()

		return lastrowid
		
	def getAll(self):
		cursor = self.db.Cursor()
		sql="select * from biscuitinfo"
		cursor.execute(sql)
		results = cursor.fetchall()

		returnArray = []
		for result in results:
			print(result)
			returnArray.append(self.convertToDictionary(result))
		cursor.close()
		
		return returnArray

    def findByID(self, id):
        cursor = self.db.Cursor()
        sql="select * from biscuitinfo where id = %s"
        values = (id,)
        cursor.execute(sql, values)
        
        result = cursor.fetchone()
        biscuit.self.convertToDictionary(result)
        cursor.close()
        return self.convertToDictionary(result)

    def update(self, values):
        cursor = self.db.cursor()
        sql="update biscuitinfo set Biscuit_Name= %s, Biscuit_Flavour= %s, Biscuit_Size= %s where id= %s"
        cursor.execute(sql, values)
        self.db.commit()
        cursor.close()

	def delete(self, id):
		cursor = self.db.cursor()	
		sql="delete from biscuitinfo where id = %s"
		values = (id,)
		
		cursor.execute(sql, values)
		self.db.commit()
		cursor.close()
		print("delete done")

	def convertToDictionary(self, result):
		colnames=['id', 'Biscuit_Name', 'Biscuit_Flavour', 'Biscuit_Size']
		print(colnames)
		item = {}
		
		if result: #if result is not empty do this..
			for i, colName in enumerate(colnames):
				print(colName)
				value = result[i]
				item[colName] = value
		
		return item

BiscuitsDAO = BiscuitsDAO()