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