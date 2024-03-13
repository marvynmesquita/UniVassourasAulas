import sqlite3
import pandas as pd
import os

os.system('del myBank.db')
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

bd = sqlite3.connect("myBank.db")

cursor = bd.cursor()

cursor.execute ("CREATE TABLE clientes (nome TEXT, idade INTEGER, cpf TEXT PRIMARY KEY, email TEXT, endereço TEXT)")
cursor.execute ("CREATE TABLE vendas (n_vendas INTEGER, desconto REAL, cpf TEXT PRIMARY KEY, id_loja INTEGER)")
cursor.execute ("CREATE TABLE lojas (id_loja INTEGER PRIMARY KEY, nome_loja TEXT, endereço TEXT, n_func INTEGER, cidade TEXT)")

cursor.execute("INSERT INTO clientes VALUES('Zé das Coves', 45, '111.444.555-22', 'zezim_das_cove22@gmail.com', 'Rua Santa Beatriz 125, Raia, Saquarema - RJ')")
cursor.execute("INSERT INTO clientes VALUES('Zé da Manga', 35, '222.451.852-31', 'zezim_da_manga22@gmail.com', 'Rua José Augusto Raia 566, Guarani, Saquarema - RJ')")
cursor.execute("INSERT INTO clientes VALUES('Tião Galinha', 50, '333.456.321-80', 'tiao_galinha22@gmail.com', 'Rua Antônio Augusto 566, Raia, Saquarema - RJ')")

cursor.execute("INSERT INTO vendas VALUES(65, 23.5, '111.444.555-22', 1)")
cursor.execute("INSERT INTO vendas VALUES(35, 8.6, '222.451.852-31', 2)")
cursor.execute("INSERT INTO vendas VALUES(12, 1.5, '333.456.321-80', 1)")

cursor.execute("INSERT INTO lojas VALUES (1, 'Loja Raia', 'Rua Santa Beatriz 185, Raia, Saquarema - RJ', 12, 'Saquarema')")
cursor.execute("INSERT INTO lojas VALUES (2, 'Loja Guarani', 'Rua SAnto Antônio 455, Guarani, Saquarema - RJ', 12, 'Saquarema')")

clear()

query = "SELECT * FROM clientes"

df_cliente = pd.read_sql_query(query, bd)
df_cliente.head()

query = "SELECT * FROM vendas"

df_vendas = pd.read_sql_query(query, bd)
df_vendas.head()

query = "SELECT * FROM lojas"

df_lojas = pd.read_sql_query(query, bd)
df_lojas.head()

query = """
    SELECT clientes.nome, vendas.n_vendas, vendas.id_loja, vendas.desconto, vendas.cpf, lojas.endereço
    FROM clientes
    JOIN vendas ON clientes.cpf
    JOIN lojas ON clientes.cpf
"""

df_join = pd.read_sql_query(query, bd)
df_join.head()

print(df_join.head())
