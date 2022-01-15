-- SQL TASKS

-- CREATE TABLE STATEMENTS

CREATE TABLE IF NOT EXISTS Cat (
	id serial PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	age INTEGER,
	favoriteFood VARCHAR(255),
	previousNames TEXT[],
	timesSpoken INTEGER
);

CREATE TABLE IF NOT EXISTS Dog (
	id serial PRIMARY KEY,
	name VARCHAR(50) NOT NULL,
	age INTEGER,
	favoriteFood VARCHAR(255),
	previousNames TEXT[],
	timesSpoken INTEGER
);

-- SAMPLE INSERT STATEMENT 

-- begin transaction
BEGIN;
INSERT INTO Cat(name, age, favoriteFood, previousNames, timesSpoken)
VALUES 
('Garfield', 40, 'Lasagna', '{"Garfield"}', 252);

INSERT INTO Dog(name, age, favoriteFood, previousNames, timesSpoken)
VALUES 
('Odie', 42, 'Anything', '{"Odie, "ScoobyDoo"}', 170);
-- commit the changes
COMMIT;