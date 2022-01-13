CREATE DATABASE IF NOT EXISTS `atividade`;
USE `atividade`;

CREATE TABLE games(
id INT(7) KEY AUTO_INCREMENT,
nome VARCHAR(80) NOT NULL,
data_lancamento DATE NOT NULL,
preco DOUBLE(6,2) NOT NULL
);
 
INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(1, "Pes21", "2020-09-15", 262.00);
 
INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(2, "Pes20", "2019-09-10", 30.00);
 
INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(3, "Clash Royale", "2016-03-02", 0.00);
 
INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(4, "Clash Of Clans", "2019-08-02", 0.00);
 
INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(5, "Free Fire", "2017-08-23", 0.00);

INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(6, "dANIEL", "2019-08-23", 0.00);

INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(7, "deNIEL", "2019-08-23", 0.00);


-- AND E OR 
SELECT id, nome FROM games WHERE preco > 0
 OR data_lancamento > '2019-01-10';

SELECT id, nome FROM games WHERE preco > 0
 AND data_lancamento > '2019-01-10';

-- comando is null
SELECT id, nome FROM games WHERE preco IS NULL;

-- like
SELECT id, nome FROM games WHERE nome NOT LIKE 'd%';