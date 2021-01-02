CREATE DATABASE Cah;
use Cah;

CREATE TABLE Users (
    id BIGINT(20) AUTO_INCREMENT,
    name VARCHAR(32),
    email VARCHAR(32),
    password VARCHAR(100),
    PRIMARY KEY(id));

INSERT INTO Users
	(name, email, password)
VALUES
	('Luiz', 'luizagnern@gmail.com', '123456'),
	('Cassio', 'cassioutfpr@gmail.com', '123456');
