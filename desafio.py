orientadores = []
alunos = []

def exibir_menu():
    print(
        f"""
        1. Cadastrar alunos e orientadores.\n
        2. Registro de versões do TCC entregues.\n
        3. Atribuição de notas por parte dos orientadores.\n
        4. Verificação de pendências de entregas por aluno.\n
        5. Relatórios para o orientador.\n
        """
    )
    
def cadastrar_orientador():
    orientador = input("Digite o nome do professor orientador: ")
    orientadores.append({orientador: []})

def funcionalidades():
    print(
        f"""
        Digite uma das opçoes:

1 - Registrar nova entrega.
2 - Registrar nota.
3 - Listar alunos por orientador.
4 - Listar versões entregues por aluno.
5 - Listar pendências de avaliação.
6 - Gerar relatório do orientador.
7 - Voltar ao menu principal.
       """
    )
    opcao_funcionalidade = input(": ")

    match opcao_funcionalidade:
        case 1:
            # Registrar nova entrega.
            return none
        case 2:
            # Registrar nota.
            return none
        case 3:
            # Listar alunos por orientador.
            return none
        case 4:
            # Listar versões entregues por aluno.
            return none
        case 5:
            # Listar pendências de avaliação.
            return none
        case 6:
            # Gerar relatório do orientador.
            return none
        case 7:
            # Voltar ao menu principal.
            return none
        case _:
            print("Default") 
            return none

def escolher_opcoes_iniciais():
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        if opcao_escolhida == 1:
            cadastrar_orientador()
        elif opcao_escolhida == 2:
            print()
            # cadastrar_aluno()
        elif opcao_escolhida == 3:
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