use Daniel_atividade3;

-- Mostrar filmes que começam com "A", "E", "I", "O" ou "U" usando o OR
SELECT * FROM filmes WHERE nome LIKE 'A%' OR nome LIKE 'E%' OR nome LIKE 'I%' OR nome LIKE 'O%' OR nome LIKE 'U%';

-- EXIBIR NOME DOS FILMES POR ORDEM ALFABETICA
SELECT * FROM filmes ORDER BY nome;

-- xibir todos os dados dos filmes ordenados de maneira decrescente pela receita de bilheteria.
SELECT * FROM filmes ORDER BY faturamento_bilheteria DESC;