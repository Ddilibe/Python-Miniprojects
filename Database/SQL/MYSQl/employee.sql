-- Creating an employee database
DROP DATABASE IF EXISTS employee;
CREATE DATABASE employee;

USE employee;

CREATE TABLE department
(
	departmentID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(30)
);

CREATE TABLE employee
(
	employeeID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(80),
	job  VARCHAR(30),
	departmentID INT NOT NULL REFERENCES department(departmentID)
);

CREATE TABLE client
(
	clientID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	name VARCHAR(40),
	address VARCHAR(100),
	contactPerson VARCHAR(80),
	contactNumber CHAR(12)
)

CREATE TABLE assignment
(
	clientID INT NOT NULL REFERENCES client(clientID),
	employeeID INT NOT NULL REFERENCES employee(employeeID),
	workdate DATE NOT NULL,
	hours FLOAT,
	PRIMARY KEY (clientID, employeeID, workdate)
);