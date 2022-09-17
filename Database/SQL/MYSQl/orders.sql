-- Questions

-- Create database with the following schema

-- customer(customerID, customerName, customerAddress)
-- order(orderID, orderDate, customerID)
-- orderItem(orderID, itemID, itemQuantity)
-- item(itemID, itemName)

-- You may make any assumptions you like about data types.
-- Test your statements in MySQL and view the resulting tables using SHOW and DESCRIBE

DROP DATABASE IF EXISTS orderS;

CREATE DATABASE orders;

USE orders;

CREATE TABLE IF NOT EXISTS customer
(
	customerID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	customerName VARCHAR(40),
	customerAddress VARCHAR(200)
);

CREATE TABLE orders
(
	orderID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	orderDate DATE,
	customerID INT NOT NULL REFERENCEs customer(customerID)
);

CREATE TABLE item
(
	itemID INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
	itemName VARCHAR(300)
);

CREATE TABLE orderItem
(
	orderID INT NOT NULL REFERENCES orders(orderID),
	itemID INT NOT NULL REFERENCES item(itemID),
	itemQuality ENUM('PERFECT', 'GOOD', 'BAD', 'WORST')
);

-- Command to show the tables
SHOW TABLES;

-- Command to show the tables in the database
DESCRIBE customer;
DESCRIBE orders;
DESCRIBE item;
DESCRIBE orderItem;

-- We would now like to add a notes field, which you may assume is of type TEXT, to each
-- order in the orders table. Use an ALTER TABLE statement to achieve this, and check your
-- result with a DESCRIBE statement.

ALTER TABLE `orders` ADD COLUMN `notes` TEXT(1000);

-- Command to delete an existing database

-- DROP DATABASE `orders`;
