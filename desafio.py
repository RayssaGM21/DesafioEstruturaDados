orientadores = []
alunos = []

def exibir_menu():
    print(
        f"""
        1. Cadastrar alunos.\n
        2. Cadastrar orientadores.\n
        3. Realizar operações.\n
        """
    )
    
def cadastrar_orientador():
    orientador = input("Digite o nome do professor orientador: ")
    orientadores.append({orientador: []})
    
def registrar_entrega():
    pass

def registrar_nota():
    pass

def escolher_opcoes_iniciais():
    try:
        opcao_escolhida = input('Escolha uma opção: ')
        if opcao_escolhida == "1":
            cadastrar_orientador()
        elif opcao_escolhida == "2":
            print()
            # cadastrar_aluno()
        elif opcao_escolhida == "3":
            print()
            # mostrar_opcoes()
        elif opcao_escolhida == "q":
            print()
            # sair()
        else:
            print()
            # opcao_invalida()
    except:
        print("")
        #  opcao_invalida()

# cadastrar_orientador()
# cadastrar_orientador()
# print(orientadores)