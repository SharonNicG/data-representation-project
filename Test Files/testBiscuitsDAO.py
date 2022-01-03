from BiscuitsDAO import BiscuitsDAO

biscuit1 = {
    'Name': 'Sunday Treat',
    'Flavour': 'Lamb',
    'Size':'Medium',
}

biscuit2 = {
    'Name': 'Post Walkies',
    'Flavour': 'Chicken',
    'Size':'Small',
}

#returnValue = BiscuitsDAO.create(book)
returnValue = BiscuitsDAO.getAll()
print(returnValue)
returnValue = BiscuitsDAO.findById(biscuit2['Name'])
print("find By Id")
print(returnValue)
returnValue = BiscuitsDAO.update(biscuit2)
print(returnValue)
returnValue = BiscuitsDAO.findById(biscuit2['Name'])
print(returnValue)
returnValue = BiscuitsDAO.delete(biscuit2['Name'])
print(returnValue)
returnValue = BiscuitsDAO.getAll()
print(returnValue)