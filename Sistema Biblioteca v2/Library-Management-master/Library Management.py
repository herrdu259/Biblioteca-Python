#Project on Library Management System
#--------------------------------------------------------------------------------
#MODULE : LIBRARY MANAGEMENT
import Database
import Menulib
import Book
import Issue

Database.DatabaseCreate()
Database.TablesCreate()


while True:
    Book.clrscreen()
    print("\t\t\t Gerenciamento da Biblioteca\n")
    print("=====================================================================")
    print("1. Gerenciamento de Livros")
    print("2. Gerenciamento de Membros")
    print("3. Emprestimo/Retorno de Livros")
    print("4. Sair")
    choice = int(input("Escolha uma opcao entre 1 e 4 ------> : "))
    if choice == 1:
        Menulib.Menubook()
    elif choice == 2:
        Menulib.MenuMember()
    elif choice == 3:
        Menulib.MenuIssueReturn()
    elif choice == 4:
        break
    else:
        print("Escolha Invalida... Selecione outra opcao")
        x = input("Pressione qualquer tecla para continuar...")
