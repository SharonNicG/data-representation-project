# Data Representation Project

The objective of this project was to write a program that demonstrates an understanding of creating and consuming RESTful APIs. 
I have chosen a simple system that allows users to record the biscuits they give their dog - inspired by Pliny, my Jack Russell/Chihuahua cross that sits at my feet while I work and loves treats.

<p align="center">
  <img src="https://github.com/SharonNicG/data-representation-project/blob/main/Pliny_JR.jpg", width=\"450\/>
</p>

Table of Contents
- [Data Representation Project](#data-representation-project)
  - [Project Overview](#project-overview)
  - [Repository Content](#repository-content)
  - [Requirements](#requirements)
  - [MySQL Database](#mysql-database)
  - [Launching the Server](#launching-the-server)
  - [Virtual Environment](#virtual-environment)
  - [Credits](#credits)

## Project Overview
This project can be accessed from the machine command line.

The project includes a web page for users to access, add, update, and delete dog biscuits. In addition, details of dog biscuits already on the system can be retrieved based on their name, flavour, size or system ID.

The data on the webpage is drawn from a MySQL Database. Information from the database tables is called by the webpage using AJAX API. The webpage can perform CRUD operations on the data.

## Repository Content

 - [staticpages folder](https://github.com/SharonNicG/data-representation-project/tree/main/staticpages) - This folder the webpages (their associated images and CSS) to be returned by the Flask server.
 - [.gitignore file](https://github.com/SharonNicG/data-representation-project/blob/main/.gitignore) - Detailing the files not to be tracked by Git.
 - [BiscuitsDAO.py](https://github.com/SharonNicG/data-representation-project/blob/main/BiscuitsDAO.py) - The Data Access Object for the RESTAPI.
 - [application.py](https://github.com/SharonNicG/data-representation-project/blob/main/application.py) - Python code for the Flask server.
 - [dbconfig.py](https://github.com/SharonNicG/data-representation-project/blob/main/dbconfig.py) - Database configuration details.
 - [initdb.sql](https://github.com/SharonNicG/data-representation-project/blob/main/initdb.sql) - .sql script for creating the database and adding additional information to it.

## Requirements
The [requirements.txt](https://github.com/SharonNicG/data-representation-project/blob/main/requirements.txt) file details the packages used to develop the project. *Note: some of these may now be redundant as there have been changes in the script.*


## MySQL Database
An instance of the [initdb.sql](https://github.com/SharonNicG/data-representation-project/blob/main/initdb.sql) MySQL Database needs to be created for the project to run.

This can be done via the bin folder of your [MySQL server](https://dev.mysql.com/downloads/mysql/) using teh command `mysql -u root -p < "C:\path\to\directory\data-representation-project/blob/main/initdb.sql"`

Or in a [MySQL terminal](https://dev.mysql.com/doc/mysql-getting-started/en/) with the command `source "C:\path\to\directory\data-representation-project\Database\G00387816_DataRepProject.sql"`

## Launching the Server
The Flask server [application.py](https://github.com/SharonNicG/data-representation-project/blob/main/application.py) can be run using the command `python application.py` from the machine command line.

Once the server runs, you will be directed to a local web page to interact with the database. To stop the server, press `ctrl + c`.

## Virtual Environment

The project can also run via the machine command line via a virtual environment.

First, the virtual environment is created with the` python -m venv venv` command. Next, the environment is run using `.\venv\Scripts\activate.bat` for Windows users or `source venv/bin/activate` on Mac/Linux.

The packages detailed in [requirements.txt](https://github.com/SharonNicG/data-representation-project/blob/main/requirements.txt) need to be loaded into the environment using the command `pip install -r requirements.txt`.

The server environment needs to be set for Flask using the `set FLASK_APP=app` command for Windows users or `export FLASK_APP=app` on Mac/Linux.

The Flask server [application.py](https://github.com/SharonNicG/data-representation-project/blob/main/application.py) can be run using the command `flask run`. Once the server runs, you will be directed to a local web page to interact with the database. To stop the server, press `ctrl + c`.

***

## Credits
 - Andrew Beatty – Lecture materials : https://learnonline.gmit.ie/course/view.php?id=3299