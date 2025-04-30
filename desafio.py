orientadores = {}
alunos = []

def exibir_menu():
    print("""
===== MENU PRINCIPAL =====
1. Cadastrar orientadores
2. Cadastrar alunos
3. Realizar operações
q. Sair
==========================
""")

def cadastrar_orientador():
    orientador = input("Digite o nome do professor orientador: ")
    if not orientador:
        print("Nome inválido.")
        return
    if orientador in orientadores:
        print("Orientador já cadastrado.")
    else:
        orientadores[orientador] = []
        print(f"Orientador '{orientador}' cadastrado com sucesso.")

def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    if not nome:
        print("Nome inválido.")
        return

    try:
        matricula = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula deve ser um número.")
        return

    if any(aluno["matricula"] == matricula for aluno in alunos):
        print("Matrícula já cadastrada.")
        return

    if not orientadores:
        print("Nenhum orientador cadastrado. Cadastre um primeiro.")
        return

    listar_orientadores()
    orientador = input("Digite o nome do orientador: ")
    if orientador not in orientadores:
        print("Orientador não encontrado.")
        return

    novo_aluno = {
        "nome": nome,
        "matricula": matricula,
        "orientador": orientador,
        "entregas": []
    }

    alunos.append(novo_aluno)
    orientadores[orientador].append(nome)
    print(f"Aluno '{nome}' cadastrado com sucesso!")

def listar_orientadores():
    print("==== Orientadores Cadastrados ====")
    if not orientadores:
        print("Nenhum orientador disponível.")
    for nome in orientadores:
        print(f"- {nome}")

def listar_alunos():
    print("==== Alunos Cadastrados ====")
    if not alunos:
        print("Nenhum aluno cadastrado.")
    for aluno in alunos:
        print(f"{aluno['nome']} | Matrícula: {aluno['matricula']} | Orientador: {aluno['orientador']}")

def registrar_entrega():
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    listar_alunos()
    try:
        matricula = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida.")
        return

    aluno = None
    for a in alunos:
        if a["matricula"] == matricula:
            aluno = a
            break

    if not aluno:
        print("Aluno não encontrado.")
        return

    if aluno["entregas"] and aluno["entregas"][-1][2] is None:
        print("A última entrega ainda não foi avaliada. Aguarde a avaliação antes de enviar nova versão.")
        return

    versao = input("Digite o nome da versão (ex: v1, v2): ")
    data = input("Digite a data (formato YYYY-MM-DD): ")
    aluno["entregas"].append((versao, data, None))
    print("Entrega registrada com sucesso!")

def registrar_nota():
    listar_orientadores()
    orientador = input("Digite seu nome (orientador): ")

    if orientador not in orientadores:
        print("Orientador não encontrado.")
        return

    alunos_orientados = [a for a in alunos if a["orientador"] == orientador]
    pendentes = []

    for aluno in alunos_orientados:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                pendentes.append((aluno, entrega))

    if not pendentes:
        print("Nenhuma entrega pendente de nota.")
        return

    print("\nEntregas pendentes:")
    for aluno, entrega in pendentes:
        print(f"Aluno: {aluno['nome']} | Matrícula: {aluno['matricula']} | Versão: {entrega[0]}")

    try:
        matricula = int(input("Digite a matrícula do aluno: "))
        versao = input("Digite a versão a ser avaliada: ")
        nota = float(input("Digite a nota: "))
    except ValueError:
        print("Erro: matrícula e nota devem ser números válidos.")
        return

    for aluno in alunos:
        if aluno["matricula"] == matricula:
            for i, ent in enumerate(aluno["entregas"]):
                if ent[0] == versao and ent[2] is None:
                    aluno["entregas"][i] = (ent[0], ent[1], nota)
                    print("Nota registrada com sucesso!")
                    return
    print("Entrega não encontrada ou já avaliada.")

def listar_alunos_por_orientador():
    listar_orientadores()
    nome = input("Digite o nome do orientador: ")
    print(f"\nAlunos do orientador {nome}:")
    for aluno in alunos:
        if aluno["orientador"] == nome:
            print(f"- {aluno['nome']} (Matrícula: {aluno['matricula']})")

def versoes_entregues_por_alunos():
    listar_alunos()
    try:
        matricula = int(input("Digite a matrícula do aluno: "))
    except ValueError:
        print("Matrícula inválida.")
        return

    aluno = None
    for a in alunos:
        if a["matricula"] == matricula:
            aluno = a
            break

    if not aluno:
        print("Aluno não encontrado.")
        return

    print(f"\nEntregas do aluno {aluno['nome']}:")
    for entrega in aluno["entregas"]:
        nota = entrega[2] if entrega[2] is not None else "Pendente"
        print(f"Versão: {entrega[0]} | Data: {entrega[1]} | Nota: {nota}")

def pendencias_de_avaliacao():
    print("==== Pendências de Avaliação ====")
    for aluno in alunos:
        for entrega in aluno["entregas"]:
            if entrega[2] is None:
                print(f"{aluno['nome']} | Versão: {entrega[0]} | Data: {entrega[1]}")

def relatorio_do_orientador():
    orientador = input("Digite o nome do orientador: ")
    if orientador not in orientadores:
        print("Orientador não encontrado.")
        return

    notas_ultimas = []
    print(f"\nRelatório do orientador {orientador}:\n")

    for aluno in alunos:
        if aluno["orientador"] == orientador:
            avaliacoes = [entrega[2] for entrega in aluno["entregas"] if entrega[2] is not None]
            if avaliacoes:
                media = sum(avaliacoes) / len(avaliacoes)
                print(f"{aluno['nome']}: média das versões = {media:.2f}")
                notas_ultimas.append(avaliacoes[-1])
            else:
                print(f"{aluno['nome']}: sem entregas avaliadas.")

    if notas_ultimas:
        media_geral = sum(notas_ultimas) / len(notas_ultimas)
        print(f"\nMédia geral da última versão avaliada de cada aluno: {media_geral:.2f}")
    else:
        print("Sem notas avaliadas para cálculo de média geral.")

def funcionalidades():
    while True:
        print("""
===== FUNCIONALIDADES =====
1. Registrar nova entrega
2. Registrar nota
3. Listar alunos por orientador
4. Listar versões entregues por aluno
5. Listar pendências de avaliação
6. Gerar relatório do orientador
q. Voltar ao menu principal
===========================
""")
        opcao = input("Escolha uma opção: ").lower()
        if opcao == "1":
            registrar_entrega()
        elif opcao == "2":
            registrar_nota()
        elif opcao == "3":
            listar_alunos_por_orientador()
        elif opcao == "4":
            versoes_entregues_por_alunos()
        elif opcao == "5":
            pendencias_de_avaliacao()
        elif opcao == "6":
            relatorio_do_orientador()
        elif opcao == "q":
            break
        else:
            print("Opção inválida.")

def escolher_opcoes_iniciais():
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ").lower()
        if opcao == "1":
            cadastrar_orientador()
        elif opcao == "2":
            cadastrar_aluno()
        elif opcao == "3":
            funcionalidades()
        elif opcao == "q":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida.")

escolher_opcoes_iniciais()
