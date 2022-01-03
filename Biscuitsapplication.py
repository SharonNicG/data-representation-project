#!flask/bin/python

# Import necessay libraries 
from flask import Flask, jsonify, request, abort, make_response, render_template, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import requests
import json
import MySQLdb.cursors
import mysql.connector
from mysql.connector import cursor
import dbconfig as cfg
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
from BiscuitsDAO import BiscuitsDAO

# Create Flask app
app = Flask(__name__, static_url_path='', static_folder='staticpages')

# Set random secret key
# https://newbedev.com/where-do-i-get-a-secret-key-for-flask
app.secret_key = 'lodr904eclb2gsvw'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'biscuits'

#init MYSQL
mysql = MySQL(app)

# Use method GET to get all data
# curl -i http://localhost:5000/biscuits
@app.route('/biscuits')
def getAll():
    if not 'username' in session:
        abort(401)
    results = BiscuitsDAO.getAll()
    return jsonify(results)

# Use method GET to find data by id 
# curl -i http://localhost:5000/biscuits/1
@app.route('/biscuits/<int:id>', methods =['GET'])
def findByID(id):
    if not 'username' in session:
        abort(401)
    foundBiscuits = BiscuitsDAO.findByID(id)
    return jsonify(foundBiscuits)

# Use method POST to input new data 
# curl -i -H "Content-Type:application/json" -X POST -d "{\"name\":\"Sunday Treat\",\"flavour\":\"Lamb\",\"size\":\"Medium\""}" http://localhost:5000/biscuits
@app.route('/biscuits', methods=['POST'])
def createbiscuit():
    if not request.json:
        abort(400)
        
    biscuit = {
        "id": request.json["id"],
        "name": request.json['name'],
        "flavour": request.json['flavour'],
        "size": request.json['size']
    }
    features = (biscuit['name'],biscuit['flavour'],biscuit['size'])
    newId = BiscuitsDAO.create(features)
    biscuit['id'] = newId
    
    return jsonify(biscuit),201

# Use method PUT to dataset 
@app.route('/biscuits/<int:id>', methods =['PUT'])
def updatebiscuit(id):
    foundBiscuit = BiscuitsDAO.findByID(id)
    if (len(foundBiscuit) == 0):
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
        
    if 'name' in reqJson:
        foundBiscuit['name'] = reqJson['name']
    if 'flavour' in reqJson:
        foundBiscuit['flavour'] = reqJson['flavour']
    if 'size' in reqJson:
        foundBiscuit['size'] = reqJson['size']
    
    features = (foundBiscuit['name'],foundBiscuit['flavour'],foundBiscuit['size'], foundBiscuit['id'])
    BiscuitsDAO.update(features)
    return jsonify(foundBiscuit)

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