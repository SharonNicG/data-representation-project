# Hanldes functions for data tables data
import mysql.connector 
# dbconfig file contains the host, user, password and database details
import dbconfig as cfg

class BiscuitsDAO:     
	db=""
	def connectToDB(self):
		self.db = mysql.connector.connect(
			host=cfg.mysql['host'],
			user=cfg.mysql['user'],
			password=cfg.mysql['password'],
			database=cfg.mysql['database']
		)
	def __init__(self):
		self.connectToDB()
		
	def getCursor(self):
		if not self.db.is_connected():
			self.connectToDB()
		return self.db.cursor()

	# Create new biscuit	
	def create(self, biscuit):
		cursor = self.getCursor()
		sql="insert into biscuits (id, name, flavour, size) values (%s, %s, %s, %s)"
		values = [
			biscuit['id'], biscuit['name'], 
			biscuit['flavour'], biscuit['size']
		]
		cursor.execute(sql, values)
		self.db.commit()
		cursor.close()
		return cursor.lastrowid
	
	# Get all the biscuits
	def getAll(self):
		cursor = self.getCursor()
		sql="select * from biscuits"
		cursor.execute(sql)
		results = cursor.fetchall()
		returnArray = []
		for result in results:
			resultAsDict = self.convertToDict(result)
			returnArray.append(resultAsDict)
		cursor.close()
		return returnArray

	# Find a biscuit by ID
	def findByID(self, id):
		cursor = self.getCursor()
		sql="select * from biscuits where id = %s"
		values = [id]
		cursor.execute(sql, values)
		result = cursor.fetchone()
		cursor.close()
		return self.convertToDict(result)

	# Find all biscuits by a particular name
	def findByID(self, name):
		cursor = self.getCursor()
		sql="select * from biscuits where name = %s"
		values = [name]
		cursor.execute(sql, values)
		result = cursor.fetchall()
		cursor.close()
		return self.convertToDict(result)

	# Find all biscuit by particular flavour
	def findByID(self, flavour):
		cursor = self.getCursor()
		sql="select * from biscuits where flavour = %s"
		values = [flavour]
		cursor.execute(sql, values)
		result = cursor.fetchall()
		cursor.close()
		return self.convertToDict(result)

	# Find all biscuit by particular size
	def findByID(self, size):
		cursor = self.getCursor()
		sql="select * from biscuits where size = %s"
		values = [size]
		cursor.execute(sql, values)
		result = cursor.fetchall()
		cursor.close()
		return self.convertToDict(result)
	
	# Update a biscuit
	def update(self, biscuit):
		cursor = self.getCursor()
		sql="update biscuit set name= %s, flavour= %s, size= %s where id= %s"
		values = [
			biscuit['id'], biscuit['name'], 
			biscuit['flavour'], biscuit['size']
		]
		cursor.execute(sql, values)
		self.db.commit()
		cursor.close()
		return biscuit

	# Delete a biscuit based on its ID
	def delete(self, id):
		cursor = self.getCursor()	
		sql="delete from biscuit where id = %s"
		values = [id]
		cursor.execute(sql, values)
		self.db.commit()
		cursor.close()
		return {}
		print("Deleted")

	# Convert list to a dictionary
	def convertToDict(self, result):
		colnames=['id', 'name', 'flavour', 'size']
		biscuit = {}
		
		if result: #if result is not empty do this..
			for i, colName in enumerate(colnames):
				value = result[i]
				biscuit[colName] = value
		return biscuit

# Instantiate BiscuitsDAO
BiscuitsDAO = BiscuitsDAO()