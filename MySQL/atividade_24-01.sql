CREATE database Daniel_atv5;
use Daniel_atv5;

CREATE Table cidades(
    id INT(7) KEY AUTO_INCREMENT,
    nome VARCHAR(80) NOT NULL,
    estado VARCHAR(2) NOT NULL,
    populacao INT(10) NOT NULL
);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(1, "São Paulo", "SP", 12000000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(2, "Rio de Janeiro", "RJ", 8000000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(3, "Belo Horizonte", "MG", 2000000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(4, "Judiaí", "SP", 425000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(5, "São Gonçalo", "RJ", 1200000);


INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(6, "Acauã", "PI", 7000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(7, "Paulistana", "PI", 20000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(8, "Patos", "PI", 6000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(9, "São João do Piauí", "PI", 10000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(10, "São Miguel do Piauí", "PI", 5000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(11, "Natal", "RN", 200000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(12, "Ceará-Mirim", "RN", 100000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(13, "Fortaleza", "CE", 1000000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(14, "Aracaju", "SE", 100000);

INSERT INTO cidades (id, nome, estado, populacao)
VALUES
(15, "Palmeira dos Índios", "AL", 100000);


-- Pesquisas

-- a) 
SELECT * FROM cidades WHERE populacao < 50000;

-- B) 
SELECT nome, estado FROM cidades;

-- C) 
SELECT nome FROM cidades WHERE nome LIKE '%o';

-- D) 
SELECT nome, estado, populacao FROM cidades WHERE estado = 'PI' AND populacao > 10000;

-- E) 
SELECT * FROM cidades ORDER BY nome;
