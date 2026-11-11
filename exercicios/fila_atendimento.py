# Fila de atendimento da Clínica Vida+

fila = []

# Inserir 3 pacientes na fila
print("=== INSERINDO PACIENTES NA FILA ===")

for i in range(3):
    print(f"\nPaciente {i + 1}:")
    nome = input("Nome: ")
    cpf = input("CPF: ")
    fila.append({"nome": nome, "cpf": cpf})

# Atender o primeiro paciente da fila
print("\n=== ATENDIMENTO ===")
primeiro = fila.pop(0)
print(f"Paciente atendido: {primeiro['nome']} | CPF: {primeiro['cpf']}")

# Mostrar quem ainda está na fila
print("\n=== PACIENTES AINDA NA FILA ===")
if not fila:
    print("Nenhum paciente restante.")
else:
    for paciente in fila:
        print(f"- {paciente['nome']} | CPF: {paciente['cpf']}")
