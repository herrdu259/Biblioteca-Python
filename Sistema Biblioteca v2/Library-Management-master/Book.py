#MODULO: LIVRO
#RESPONSAVEL PELO PROCESSAMENTO DOS DADOS DE LIVROS NO BD.
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os
import platform


def clrscreen():
    if platform.system() == "Windows":
        print(os.system("cls"))


#FUNÇÃO RESPONSAVEL PELA INSERÇÃO DE UM LIVRO NO BD.
def inserirDados():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        livroCod = input("Insira o Codigo do Livro : ")
        livroNome = input("Insira o Nome do Livro : ")
        Autor = input("Insira o Nome do Autor do Livro : ")
        preco = int(input("Insira o Preco do Livro : "))
        publ = input("Insira a Editora do Livro : ")
        qtd = int(input("Insira a Quantidade Comprada : "))
        print("Insira a Data da Compra (Dia, Mes e Ano separadamente!) : ")
        DD = int(input("Insira o Dia : "))
        MM = int(input("Insira o Mes : "))
        YY = int(input("Insira o Ano : "))
        Qry = ("INSERT INTO LivroRegistro VALUES (%s, %s, %s, %s, %s, %s, %s)")
        data = (livroCod, livroNome, Autor, preco, publ, qtd, date(YY,MM,DD))
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Record Inserted.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
    cnx.close()


#FUNÇÃO RESPONSAVEL POR DELETAR UM LIVRO DO BD.
def deletarLivro():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        livroCod = input("Insira o Codigo do Livro para deletar : ")
        Qry = ("""DELETE FROM LivroRegistro WHERE livroCod = %s""")
        del_reg = (livroCod,)
        Cursor .execute(Qry, del_reg)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Registro Detelado com Sucesso.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
    cnx.close()

#FUNÇÃO RESPONSAVEL PELA PROCURA DE UM LIVRO NO BD.
def buscarRegLivro():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()

        livroCod = input("Insira o Codigo do Livro a ser pesquisado na biblioteca : ")

        query = ("SELECT * FROM livroregistro WHERE livroCod = %s ")
        reg_proc = (livroCod)

        Cursor.execute(query, reg_proc)
        Rec_count = 0

        for(livroCod, livroNome, Autor, preco, publ, qtd, data_compra) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Codigo do Livro : ", livroCod)
            print("Nome do Livro : ", livroNome)
            print("Autor do Livro : ", Autor)
            print("Preco do Livro : ", preco)
            print("Editora do Livro : ", publ)
            print("Quantidade total em estoque : ", qtd)
            print("Comprado em : ", data_compra)
            print("=============================================================")
            if Rec_count % 2 == 0:
                input("Pressione qualquer teclado para continuar...")
                clrscreen()
                print(Rec_count, "Registro(s) Encontrado.")
        cnx.commit()
        Cursor.close()
        cnx.close()
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
        cnx.close()


#FUNÇÃO RESPONSAVEL PELA ATUALIZAÇÃO DE DADOS DE UM LIVRO NO BD.
def AtualizarLivro():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()

        livroCod = input("Insira o Codigo do Livro para atualizar o seu registro na biblioteca : ")
        
        
        print("Insira os novos dados")
        livroNome = input("Insira o Nome do Livro : ")
        Autor = input("Insira o Nome do Autor do Livro : ")
        preco = int(input("Insira o Preco do Livro : "))
        publ = input("Insira a Editora do Livro : ")
        qtd = int(input("Insira a Quantidade Comprada : "))
        print("Insira a Data da Compra (Dia, Mes e Ano separadamente!) : ")
        DD = int(input("Insira o Dia : "))
        MM = int(input("Insira o Mes : "))
        YY = int(input("Insira o Ano : "))
        data_compra = date(YY,MM,DD)
        Qry = ("UPDATE LivroRegistro SET livroNome=%s, Autor=%s, preco=%s, publ=%s, qtd=%s, data_compra=%s WHERE livroCod=%s")
        data = (livroNome, Autor, preco, publ, qtd, data_compra, livroCod)
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "O registro foi atualizado com sucesso.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
    cnx.close()
