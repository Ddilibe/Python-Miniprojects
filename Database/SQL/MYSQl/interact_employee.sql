-- Interacting with an employee database
-- Inserting data into the database

-- The employee database already exist
USE employee;

-- 
DELETE FROM department;

INSERT INTO department VALUES
(42, 'Finance'),
(128, 'Research and Development'),
(NULL, 'Human Resources'),
(NULL, 'Marketing')
;

DELETE FROM employee;

INSERT INTO employee VALUES
(7513, 'Nora Edwards', 'Programmer', 128),
(9842, 'Ben Smith', 'DBA', 42),
(6651, 'Ajay Patel', 'Programmer', 128),
(9006, 'Candy Burnett', 'Systems Administrator', 128)
;

DELETE FROM employeeSkills;

INSERT INTO employeeSkills VALUES
(7513, 'C'),
(7513, 'Perl'),
(7513, 'Java'),
(9842, 'DB2'),
(6651, 'VB'),
(6651, 'Java'),
(9006, 'NT'),
(9006, 'Linux');

DELETE FROM client;

INSERT INTO client VALUES
(NULL, 'Telco Inc', '1 Collins St Melbourne', 'Fred Smith', '95551234'),
(NULL, 'The Bank', '100 Bourke St Melbourne', 'Jan Tristan', '95569876');

DELETE FROM assignment;

INSERT INTO assignment VALUES
(1, 7513, '2003-01-20', 8.5);
