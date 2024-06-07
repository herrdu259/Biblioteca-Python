#MODULO: EMPRESTIMO
#RESPONSAVEL PELO PROCESSAMENTO DOS EMPRESTIMOS DE LIVROS NO BD.
import mysql.connector
from mysql.connector import errorcode
from datetime import date
from mysql.connector import (connection)
import os


def clrscreen():
    print('\n' * 5)


def issueBook():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        livroCod = input("Insira o Codigo do Livro para o Emprestimo : ")
        membroCod = input("Insira o Codigo do Membro para o Emprestimo  : ")
        print("Insira a Data do Emprestimo (Dia, Mes e Ano separadamente!)) : ")
        DD = int(input("Insira o Dia : "))
        MM = int(input("Insira o Mes : "))
        YY = int(input("Insira o Ano : "))
        Qry = ("INSERT INTO emprestimo (livroCod,membroCod,dataEmprestimo) VALUES(%s, %s, %s) ")
        data = (livroCod,membroCod,date(YY,MM,DD))
        Cursor.execute(Qry,data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Recorded Inserted.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
    cnx.close()


def SearchIssuedBooks():
    try:
        os.system('cls')
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        membroCod = input("Insira o Codigo do Membro para pesquisar seus emprestimos: ")
        query = ("SELECT * FROM emprestimo where membroCod = %s")
        reg_proc = (membroCod,)
        Cursor.execute(query, reg_proc)
        Rec_count = 0
        for (livroCod,membroCod,dataEmprestimo,dataEmprestimoRetorno) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("1.Codigo do Livro : ", livroCod)
            print("2.Codigo do Membro : ", membroCod)
            print("3.Data do Emprestimo : ", dataEmprestimo)
            print("4.Data do Retorno do Emprestimo : ", dataEmprestimoRetorno)
            print("=============================================================")
            if Rec_count%2 == 0:
                input("Pressione qualquer teclado para continuar...")
                clrscreen()
                print(Rec_count, "Registro(s) Encontrado.")
        Cursor.close()
        cnx.close()
        print("Pesquisa concluida!")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
    else:
        cnx.close()


def returnBook():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        livroCod = input("Insira o Codigo do Livro que vai ser Retornado a biblioteca : ")
        membroCod = input("Insira o Codigo do Membro que esta Retornado o livro a biblioteca : ")
        retDate = date.today()
        Qry = ("""Update emprestimo set dataEmprestimoRetorno = %s WHERE livroCod = %s and membroCod = %s""")
        rec = (retDate, livroCod, membroCod)
        Cursor.execute(Qry, rec)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print(Cursor.rowcount, "Record(s) Deleted Successfully.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
        cnx.close()
