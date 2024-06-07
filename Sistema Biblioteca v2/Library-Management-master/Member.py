#MODELU: MEMBRO
#RESPONSAVEL PELO PROCESSAMENTO DOS DADOS DOS MENBROS DA BIBLIOTECA NO BD.
import mysql.connector
from mysql.connector import errorcode
from datetime import date, datetime, timedelta
from mysql.connector import(connection)
import os


def clrscreen():
    print('\n' * 5)


#FUNÇÃO RESPONSAVEL POR INSERIR UM NOVO MEMBRO NO BD.
def inserirMembro():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        membroCod = input("Insira o Codigo do Membro : ")
        membroNome = input("Insira o Nome do Membro : ")
        print("Insira a Data de Cadastro (Dia, Mes e Ano separadamente!)  : ")
        DD = int(input("Insira o Dia: "))
        MM = int(input("Insira o Mes: "))
        YY = int(input("Insira o Ano: "))
        membroEndereco = input("Insira o Endereco : ")
        celular = int(input("Insira o Numero de Celular: "))
        Qry = ("INSERT INTO Membros VALUES(%s, %s, %s, %s, %s)")
        data = (membroCod,membroNome,date(YY,MM,DD),membroEndereco,celular)
        Cursor.execute(Qry, data)
        cnx.commit()
        Cursor.close()
        cnx.close()
        print("Dados Inseridos.")
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Algo esta errado com o seu usuario e senha BD!")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database nao existe!")
        else:
            print(err)
    cnx.close()


#FUNÇÃO RESPONSAVEL POR DELETAR UM MEMBRO DO BD.
def deletarMembro():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        membroCod = input("Insira o Codigo do Membro que deseja Deletar da biblioteca: ")
        Qry =("""DELETE FROM Membros WHERE membroCod = %s""")
        del_reg = (membroCod,)
        Cursor.execute(Qry, del_reg)
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


#FUNÇÃO RESPONSAVEL POR PROCURAR UM MEMBRO NO BD.
def procurarMembro():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        mnm = input("Insira o Codigo do Membro a ser Pesquisado na biblioteca : ")
        query = ("SELECT * FROM Membros where membroCod = %s")
        reg_proc = (mnm,)
        Cursor.execute(query, reg_proc)
        Rec_count = 0
        for(membroCod, membroNome, dataRegMembro, membroEndereco, celular) in Cursor:
            Rec_count += 1
            print("=============================================================")
            print("Codigo do Membro : ", membroCod)
            print("Nome do Membro : ", membroNome)
            print("Data de Registro : ", dataRegMembro)
            print("Endereco do Membro : ", membroEndereco)
            print("Celular : ", celular)
            print("=============================================================")
            if Rec_count%2 == 0:
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


#FUNÇÃO RESPONSAVEL POR ATUALIZAR OS DADOS DE UM MEMBRO NO BD.
def AtualizarMembro():
    try:
        cnx = mysql.connector.connect(user='root', password='s9k35t8hbd', host='localhost', database='Library')
        Cursor = cnx.cursor()
        membroCod = input("Enter Member Code of Member to be Updated from the Library : ")
        query = ("SELECT * FROM Membros WHERE membroCod = %s")
        reg_proc = (membroCod,)
        print("Enter new data")
        membroNome = input("Insira o Nome do Membro : ")
        print("Insira a Data de Cadastro (Dia, Mes e Ano separadamente!)  : ")
        DD = int(input("Insira o Dia: "))
        MM = int(input("Insira o Mes: "))
        YY = int(input("Insira o Ano: "))
        membroEndereco = input("Insira o Endereco : ")
        celular = int(input("Insira o Numero de Celular: "))
        dataRegMembro = date(YY,MM,DD)
        Qry = ("UPDATE Membros SET membroNome=%s, dataRegMembro=%s, membroEndereco=%s, celular=%s WHERE membroCod=%s")
        data = (membroNome,dataRegMembro,membroEndereco,celular,membroCod)
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
