# ============================================
# SISTEMA CLÍNICA VIDA+ — Gestão de Pacientes
# ============================================

pacientes = []


# ---------------------------
# Função: Cadastrar Paciente
# ---------------------------
def cadastrar():
    print("\n=== CADASTRAR PACIENTE ===")

    nome = input("Nome: ").strip()
    while nome == "":
        print("O nome não pode estar vazio.")
        nome = input("Nome: ").strip()

    # Validação da idade
    while True:
        try:
            idade = int(input("Idade: "))
            if idade <= 0:
                print("A idade deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Idade inválida! Digite um número.")

    telefone = input("Telefone: ").strip()
    while telefone == "":
        print("O telefone não pode estar vazio.")
        telefone = input("Telefone: ").strip()

    pacientes.append({"nome": nome, "idade": idade, "telefone": telefone})
    print("Paciente cadastrado com sucesso!\n")


# ---------------------------
# Função: Estatísticas
# ---------------------------
def estatisticas():
    print("\n=== ESTATÍSTICAS ===")

    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    total = len(pacientes)
    media = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda p: p["idade"])
    mais_velho = max(pacientes, key=lambda p: p["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media:.1f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")


# ---------------------------
# Função: Buscar Paciente
# ---------------------------
def buscar():
    print("\n=== BUSCAR PACIENTE ===")

    nome = input("Digite o nome: ").strip().lower()
    encontrados = [p for p in pacientes if p["nome"].lower() == nome]

    if encontrados:
        print("\nPaciente(s) encontrado(s):")
        for p in encontrados:
            print(f"- {p['nome']} | {p['idade']} anos | {p['telefone']}")
    else:
        print("Paciente não encontrado.")

    print()


# ---------------------------
# Função: Listar Pacientes
# ---------------------------
def listar():
    print("\n=== LISTA DE PACIENTES ===")

    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    for p in pacientes:
        print(f"- {p['nome']} | {p['idade']} anos | {p['telefone']}")

    print()


# ---------------------------
# Menu Principal
# ---------------------------
while True:
    print("\n======================================")
    print("      SISTEMA CLÍNICA VIDA+")
    print("======================================")
    print("1. Cadastrar paciente")
    print("2. Ver estatísticas")
    print("3. Buscar paciente")
    print("4. Listar todos os pacientes")
    print("5. Sair")
    print("======================================")

    opc = input("Escolha uma opção: ")

    if opc == "1":
        cadastrar()
    elif opc == "2":
        estatisticas()
    elif opc == "3":
        buscar()
    elif opc == "4":
        listar()
    elif opc == "5":
        print("Encerrando o sistema... Até logo!")
        break
    else:
        print("Opção inválida! Tente novamente.\n")