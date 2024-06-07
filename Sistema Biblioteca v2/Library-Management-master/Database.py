"""CREATING DATABASES AND ALL THE REQUIRED TABLES NEEDED TO RUN THE PROJECT
DATABASE NAME: Library
TABLES: LivroRegistro, Membros, Issue"""

import mysql.connector

def DatabaseCreate():
    cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE DATABASE IF NOT EXISTS Library")
    Cursor.execute("")
    Cursor.close()
    cnx.close()


def TablesCreate():
    cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
    Cursor = cnx.cursor()
    Cursor.execute("CREATE TABLE IF NOT EXISTS LivroRegistro(livroCod int(2), livroNome varchar(20), Autor varchar(20), preco int(3), Publ varchar(20), qtd int(2), data_compra Date)")
    Cursor.execute("CREATE TABLE IF NOT EXISTS Membros(membroCod int(2), membroNome varchar(20), dataRegMembro Date, membroEndereco varchar(24), celular varchar(10))")
    Cursor.execute("CREATE TABLE IF NOT EXISTS emprestimo(livroCod int(2), membroCod int(2), dataEmprestimo Date, dataEmprestimoRetorno Date)")
    Cursor.close()
    cnx.close()
