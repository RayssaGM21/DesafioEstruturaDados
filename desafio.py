orientadores = [{"Teste": "Matheus Teste"}]
alunos = [{"nome": "Matheus Teste",
     "matricula": 101010,
     "orientador": "Teste",
     "entregas":[
         ("v1", "24/04/2025", None),
     ]}]


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
    orientadores[orientador] = []

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    matricula = int(input("Digite a matricula do aluno: "))
    orientador = input("Digite o nome do orientador: ")
    entregas = []
    aluno = {"nome": nome,
     "matricula": matricula,
     "orientador": orientador,
     "entregas": entregas}
    alunos.append(aluno)
    print(alunos)
    
def registrar_entrega():
    listar_alunos()

    print("Selecione o aluno pela matricula: ")

    matricula = input(": ")

    versao = input("Nome da Versão:     (Exemplos [v2, v3])")

    data = input ("Digite a Data: ")
    
    for i in alunos:
        if i['matricula'] == matricula:
            i['entregas'].append((versao,data,None))

def registrar_nota():
    listar_orientadores()
    print("Se identifique como orientador digitando seu Nome")

    orientador_nome = input(": ")
    alunos_deste_orietador = []
    alunos_sem_nota = []
    

    for i in alunos:
        if i['orientador'] == orientador_nome:
            alunos_deste_orietador.append(i)
    for i in alunos_deste_orietador:
        for i2 in i['entregas']:
                if i2[2] is None:
                    alunos_sem_nota.append({
                        "nome": i['nome'],
                        "matricula": i['matricula'],
                        "entregas": (i2[0], i2[1], i2[2])
                    })
    print("Alunos e suas Entregas sem Nota")
    for i in alunos_sem_nota:
        print(
            f"""
            Aluno: {i['nome']}
            Matrícula: {i['matricula']}
            Versão: {i['entregas'][0]}
            Nota: Sem nota.
            """
        )
    print("Escolha o Aluno pela Matrícula")
    matricula = input(": ")
    print("Escolha qual a entrega será atribuida a nota")
    versao = input(": ")
    nota = input("Nota: ")

    for i in alunos:
        if i["matricula"] == int(matricula):
            for index, i2 in enumerate(i["entregas"]):
                if i2[0] == versao:
                    nova_entrega = (versao, i2[1], nota)
                    i["entregas"][index] = nova_entrega

def listar_alunos_por_orientador():
    listar_orientadores()
    print("Escolha um orientador pelo nome")
    nome = input(": ")

    alunos_do_orientador = []

    for i in alunos:
        if i["orientador"] == nome:
            alunos_do_orientador.append(i)
    
    print(f"Lista de Alunos do Orientador: [{nome}]")
    for i in alunos_do_orientador:
        print("==================================")
        print(f"Nome: {i["nome"]}")
        print(f"Matrícula: {i["matricula"]}")
        print("==================================")

def relatorio_do_orientador ():
    print("Identifique o orientador pelo nome: ")
    orientador = input(">")
    alunos_do_orientador = []
    alunos_sem_nota = []

    for i in alunos:
        if i['orientador'] == orientador:
            alunos_do_orientador.append(i)

    print(f"O orientador {orientador} tem como orientandos os alunos: ")
    for aluno in alunos_do_orientador:
        print(aluno)


    for y in alunos_do_orientador:
        for z in y['entregas']:
                if z[2] is None:
                    alunos_sem_nota.append({
                        "nome": y['nome'],
                        "matricula": y['matricula'],
                        "entregas": (z[0], z[1], z[2])
                    })
    
    print(f"O orientador {orientador} possui {len(alunos_sem_nota)} alunos sem nota!")
    
    



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
            registrar_entrega()
        case 2:
            registrar_nota()
        case 3:
            # Listar alunos por orientador.
            return None
        case 4:
            # Listar versões entregues por aluno.
            return None
        case 5:
            # Listar pendências de avaliação.
            return None
        case 6:
            # Gerar relatório do orientador.
            return None
        case 7:
            # Voltar ao menu principal.
            return None
        case _:
            print("Default") 
            return None

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


def listar_orientadores():
    print("==== Lista de Orientadores ====")
    for i in orientadores:
        print(f"           {i}            ")
    print("===============================")


def listar_alunos():
    print("==== Lista de Alunos ====")
    for i in alunos:
        print(f"           {i['nome']}            ")
        print(f"           {i['matricula']}            ")
        print(f"           {i['orientador']}            ")
        print(f"           {i['entregas']}            ")
    print("===============================")


# cadastrar_orientador()
# cadastrar_orientador()
# print(orientadores)

listar_alunos_por_orientador()