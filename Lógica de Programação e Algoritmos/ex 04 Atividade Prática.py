# Boas vindas
print("Bem vindo(a) á livraria da Sarah Marques!")
lista_livro = []
id_global = 0

# Cadastra novos livros
def cadastrar_livro(id_global):
    print('''
    ------ MENU CADASTRAR LIVRO -----
    ---------------------------------
    ''')
    id = input("Insira o id do livro: ")
    nome = input("Insira o nome do livro: ")
    autor = input("Insira o autor: ")
    editora = input("Insira a editora: ")

    # Adiciona as informações no dicionário abaixo
    livro = {"id": id_global, "nome": nome, "autor": autor, "editora": editora}

    # Insere os cadastros dentro da lista_livro
    lista_livro.append(livro)


# Consulta livros cadastrados
def consultar_livro():

    while True:
        try:
            print('''
    ------ MENU CONSULTAR LIVRO -----
    ---------------------------------
    1 - Consultar todos os Livros
    2 - Consultar Livro por ID
    3 - Consultar Livro(s) por autor
    4 - Retornar
    ---------------------------------
            ''')
            consultar_opcao = int(input("Digite a opção desejada: "))

            if consultar_opcao in [1, 2, 3, 4]:
                break
            else:
                print("Opção inválida")
        except ValueError:
            print("Opção inválida")

    # Exibe todos os livros cadastrados
    if consultar_opcao == 1:
        for listagem in lista_livro:
            print(f" \n ID: {listagem['id']} \n Livro: {listagem['nome']} \n Autor: {listagem['autor']} \n Editora: {listagem['editora']}\n")

    # Exibe livros cadastrados pelo ID
    elif consultar_opcao == 2:
        try:
            consultar_opcao_id = int(input("Insira o ID: "))
            for listagem in lista_livro:
                if listagem["id"] == consultar_opcao_id: #Formatação feita para exibir as informações em linhas
                    print(f" \n ID: {listagem['id']} \n Livro: {listagem['nome']} \n Autor: {listagem['autor']} \n Editora: {listagem['editora']}\n")
        except ValueError:
            print("Opção Inválida")

    # Exibe livros cadastrados por autor
    elif consultar_opcao == 3:
            consultar_opcao_autor = input("Insira o autor: ")
            for listagem in lista_livro:
                if listagem["autor"] == consultar_opcao_autor:
                    print(f" \n ID: {listagem['id']} \n Livro: {listagem['nome']} \n Autor: {listagem['autor']} \n Editora: {listagem['editora']}\n")
    # Volta ao menu principal
    elif consultar_opcao == 4:
        return

    # Volta ao menu de consulta de livros ao invés do menu principal
    consultar_livro()

# Remove livros cadastrados
def remover_livro():
    while True:
        try:
            print('''
    ------- MENU REMOVER LIVRO ------
    ---------------------------------
    ''')
            remover_livro_id = int(input("Insira o ID do livro a ser removido: "))
        except ValueError:
            print("ID inválido, Tente novamente.")
            remover_livro_id = int(input("Insira o ID do livro a ser removido: "))

        # Dicionários são listados, se haver correspondência do ID inserido com o ID cadastrado, o livro é removido do dicionário e volta ao menu principal
        for listagem in lista_livro:
            if listagem["id"] == remover_livro_id:
                lista_livro.remove(listagem)
                print("Livro removido com sucesso!")
                return
        else:
            # Se o livro não for encontrado, volta ao início do loop
            print("Livro não encontrado")
            continue

# Mantém o menu principal rodando
while True:
    print('''
    --------- MENU PRINCIPAL --------
    ---------------------------------
    1 - Cadastrar Livro
    2 - Consultar Livro(s)
    3 - Remover Livro
    4 - Sair
    ---------------------------------
    ''')

    opcao = input("Digite a opção desejada: ")
    while opcao not in ["1", "2","3", "4"]:
        opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        # Adiciona +1 no id_global, indicando o ID do livro, adicionando +1 sempre que um novo livro é cadastrado
        id_global += 1
        cadastrar_livro(id_global)
    elif opcao == "2":
        consultar_livro()
    elif opcao == "3":
        remover_livro()
    elif opcao == "4":
        print("Saindo...")
        break
    else:
        print("Opção inválida")