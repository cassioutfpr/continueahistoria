CREATE DATABASE Cah;
use Cah;

CREATE TABLE Users (id VARCHAR(32),name VARCHAR(32),email VARCHAR(32),password VARCHAR(100));

INSERT INTO Users
	(id, name, email, password)
VALUES
	('001', 'Luiz', 'luizagner@gmail.com', '123456'),
	('002', 'Cassio', 'cassioutfpr@gmail.com', '123456');