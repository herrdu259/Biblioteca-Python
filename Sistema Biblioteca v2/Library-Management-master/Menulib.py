#PYTHN MODULE: MENULIB
import Book
import Member
import Issue

def Menubook():
    while True:
        Book.clrscreen()
        print("\t\t\t Gerenciamento de Registro de Livros\n")
        print("==========================================================")
        print("1. Adicionar um Livro")
        print("2. Pesquisar um Livro")
        print("3. Deletar um Livro")
        print("4. Atualizar um Livro")
        print("5. Retornar ao Menu Principal")
        print("==========================================================")
        choice = int(input("Escolha uma opcao entre 1 e 5 ------> : "))
        if choice == 1:
            Book.inserirDados()
        elif choice == 2:
            Book.buscarRegLivro()
        elif choice == 3:
            Book.deletarLivro()
        elif choice == 4:
            Book.AtualizarLivro()
        elif choice == 5:
            return
        else:
            print("Escolha Invalida... Selecione outra opcao")
            x = input("Pressione qualquer tecla para continuar...")

def MenuMember():
    while True:
        Book.clrscreen()
        print("\t\t\t Gerenciamento de Registro de Membros\n")
        print("==========================================================")
        print("1. Adicionar um Membro")
        print("2. Pesquisar um Membro")
        print("3. Deletar um Membro")
        print("4. Atualizar um Membro")
        print("5. Retornar ao Menu Principal")
        print("==========================================================")
        choice = int(input("Escolha uma opcao entre 1 e 5 ------> : "))
        if choice == 1:
            Member.inserirMembro()
        elif choice == 2:
            Member.procurarMembro()
        elif choice == 3:
            Member.deletarMembro()
        elif choice == 4:
            Member.AtualizarMembro()
        elif choice == 5:
            return
        else:
            print("Escolha Invalida... Selecione outra opcao")
            x = input("Pressione qualquer tecla para continuar...")

def MenuIssueReturn():
    while True:
        Book.clrscreen()
        print("\t\t\t Gerenciamento de Registro de Emprestimos\n")
        print("==========================================================")
        print("1. Emprestimo de um Livro")
        print("2. Pesquisar Registros de Emprestimos")
        print("3. Devolucao de um Livro")
        print("4. Retornar ao Menu Principal")
        print("==========================================================")
        choice = int(input("Escolha uma opcao entre 1 e 4 ------> : "))
        if choice == 1:
            Issue.issueBook()
        elif choice == 2:
            Issue.SearchIssuedBooks()
        elif choice == 3:
            Issue.returnBook()
        elif choice == 4:
            return
        else:
            print("Escolha Invalida... Selecione outra opcao")
            x = input("Pressione qualquer tecla para continuar...")
