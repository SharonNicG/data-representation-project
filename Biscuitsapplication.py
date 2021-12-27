#!flask/bin/python

# Import necessay libraries 
from flask import Flask, jsonify,  request, abort, make_response, render_template, redirect, url_for, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from BiscuitsDAO import BiscuitsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

nextId=3

# Use method GET to get all data
# curl -i http://localhost:5000/biscuits
@app.route('/biscuits')
def getAll():
    results = BiscuitsDAO.getAll()
    return jsonify(results)

# Use method GET to find data by id 
# curl -i http://localhost:5000/biscuits/1
@app.route('/biscuits/<int:id>', methods =['GET'])
def findByID(id):
    foundBiscuits = BiscuitsDAO.findByID(id)
    return jsonify(foundBiscuits)

# Use method POST to input new data 
# curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Sunday Treat\",\"flavour\":\"Lamb\",\"size\":\"Medium\""}" http://localhost:5000/biscuits
@app.route('/biscuits', methods=['POST'])
def createbiscuit():
    if not request.json:
        abort(400)
        
    biscuits = {
        "name": request.json['name'],
        "flavour": request.json['flavour'],
        "size": request.json['size']
    }
    features = (biscuits['name'],biscuits['flavour'],biscuits['size'])
    newId = BiscuitsDAO.create(features)
    biscuits['id'] = newId
    
    return jsonify(biscuits),201

# Use method PUT to dataset 
@app.route('/biscuits/<int:id>', methods =['PUT'])
def updatebiscuit(id):
    foundBiscuits = BiscuitsDAO.findByID(id)
    if (len(foundBiscuits) == 0):
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
        
    if 'name' in reqJson:
        foundBiscuits['name'] = reqJson['name']
    if 'flavour' in reqJson:
        foundBiscuits['flavour'] = reqJson['flavour']
    if 'size' in reqJson:
        foundBiscuits['size'] = reqJson['size']
    
    features = (foundBiscuits['name'],foundBiscuits['flavour'],foundBiscuits['size'], foundBiscuits['id'])
    BiscuitsDAO.update(features)
    return jsonify(foundBiscuits)

# Use method DELETE to delete dataset
@app.route('/biscuits/<int:id>', methods =['DELETE'])
def deleteBiscuits(id):
    BiscuitsDAO.delete(id)
        
    return  jsonify( { 'Completed':True })

# Use method Get and POST for Login
@app.route('/login/', methods=["GET","POST"])
def login_page():

    error = ''
    try:
	
        if request.method == "POST":
		
            attempted_username = request.form['username']
            attempted_password = request.form['password']

            if attempted_username == "admin" and attempted_password == "password":
                return redirect(url_for('dashboard'))				
            else:
                error = "Invalid. Try Again."

        return render_template("login.html", error = error)

    except Exception as e:
        return render_template("login.html", error = error)  
		

# Error Handling
@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__':
    app.run(debug= True)