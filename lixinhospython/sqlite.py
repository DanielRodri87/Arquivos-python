import sqlite3

banco = sqlite3.connect('primeiro_banco.db')
cursor = banco.cursor()

class funcoes:

    def dell():
        try: 
            cursor.execute("DELETE from pessoas WHERE idade = 50")
            banco.commit()
            banco.close()
            print("Os dados foram apagados")

        except sqlite3.Error as erro: 
            print("Deu ruim meu caro.Ti vira.", erro)
    
    def insert():
        try:
            cursor.execute("INSERT INTO pessoas VALUES('Teste', 50, 'carlos899@gmail.com')")
            banco.commit()
            print("Deu bom")

        except sqlite3.Error as erro:
            print("Não foi dessa vez meu caro, da um jeito aí", erro)