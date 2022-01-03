CREATE DATABASE biscuits;

USE biscuits;

CREATE TABLE users (
    id int(11) NOT NULL AUTO_INCREMENT,
    username VARCHAR (250),
    pass VARCHAR (250),
    PRIMARY KEY(id));

INSERT INTO users (username, pass)
Values ( 'user1', 'pass1');

INSERT INTO users (username, pass)
Values ( 'user2', 'pass2');

CREATE TABLE biscuits (
    id int(250) NOT NULL,
    name VARCHAR (250),
    flavour VARCHAR (250),
    size VARCHAR (250),
    PRIMARY KEY(id)
);

INSERT INTO biscuits VALUES
('0001', 'Sunday Treat', 'Lamb', 'Medium'),
('0002', 'Post Walkies', 'Chicken', 'Small'),
('0003', 'Night Time', 'Veggie', 'Small'),

