#!flask/bin/python

# Import necessary libraries 
from flask import Flask, jsonify, request, abort, make_response, render_template, redirect, url_for, flash, session
from flask_mysqldb import MySQL
import requests
import JSON
import MySQLdb.cursors
import MySQL.connector
from MySQL.connector import cursor
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

# Initiatie MYSQL
mysql = MySQL(app)

# Authorise User Login
# https://pythonbasics.org/flask-sessions/
# https://flask.palletsprojects.com/en/2.0.x/quickstart/
@app.route('/')
def root():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('index.html')

# Use method Get and POST for Login
# https://realpython.com/introduction-to-flask-part-2-creating-a-login-page/
# https://flask-login.readthedocs.io/en/latest/
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cur.execute("select username,pass from users where username=%s", [username])
        user = cur.fetchone()
        if user:
            session['loggedin'] = True
            session['username'] = user['username']
            return render_template('Homepage.html', username=username)
        else:
            flash('Invalid Details. Please Try Again.')
            return render_template('Loginpage.html')
    else:
        return render_template('Loginpage.html')

# Logging Out
@app.route('/logout')
def logout():
    session.clear()
    return render_template('Loginpage.html')

# Homepage
@app.route('/homepage')
def home():
    if not 'username' in session:
        return redirect(url_for('login'))
    return render_template('Homepage.html')

# Use method GET to get all data
@app.route('/biscuits')
def getAll():
    if not 'username' in session:
        abort(401)
    results = BiscuitsDAO.getAll()
    return jsonify(results)

# Use method GET to find data by id 
@app.route('/biscuits/<int:id>', methods =['GET'])
def findByID(id):
    if not 'username' in session:
        abort(401)
    foundBiscuits = BiscuitsDAO.findByID(id)
    return jsonify(foundBiscuits)

# Use method POST to input new data 
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

# Error Handling
@app.errorhandler(400)
def not_found400(error):
    return make_response( jsonify( {'error':'Bad Request' }), 400)

if __name__ == '__main__':
    app.run(debug= True)