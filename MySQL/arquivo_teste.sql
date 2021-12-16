CREATE DATABASE IF NOT EXISTS `arquivo_teste3`;
USE `arquivo_teste3`;

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
(4, "Clash Of Clans", "2012-08-02", 0.00);
 
INSERT INTO games (id, nome, data_lancamento, preco)
VALUES
(5, "Free Fire", "2017-08-23", 0.00);

-- Imprimir tabela
SELECT * FROM games;

