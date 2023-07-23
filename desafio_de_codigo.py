def depositar(saldo, valor, extrato,/):

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*,saldo, limite, extrato, numero_saques, LIMITE_SAQUES, valor):
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")

    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")

    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")

    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def mostrar_extrato(saldo,/,*, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios):
    cpf = input ("Informe seu CPF(somente números): ")
    usuario = filtrar_usuario (cpf,usuarios)

    if usuario:
        print ("Usuário já existente")

    nome = input("Qual é seu nome completo: \n")
    data_de_nascimento = input("Qual é a sua data de nascimento? (dd-mm-aaaa): \n")
    logradouro = input("Qual é seu endereço? (Logradouro, número - bairro - cidade/sigla do estado): \n")

    usuarios.append ({"nome":nome, "data_de_nascimento":data_de_nascimento,"cpf":cpf,"logradouro":logradouro})

    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf,usuarios):
    filtro = [localiza_cpf for localiza_cpf in usuarios if localiza_cpf["cpf"] == cpf]
    return filtro[0] if filtro else None

def listar_usuarios(usuarios):
    for usuario in usuarios:
        mensagem = f'''
Usuário: {usuario['nome']}
Data de Nascimento: {usuario['data_de_nascimento']} \n
'''
        print ("-"*70)
        print (mensagem)
        
def criar_conta(agencia,numero_conta,usuarios, contas):
    cpf = input ("Informe seu CPF(somente números): ")
    usuario = filtrar_usuario (cpf,usuarios)
    
    
    if usuario:
        print ("Conta criada com sucesso")
        contas.append ({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
        numero_conta += 1
    else:
        print("Usuario não localizado, encerrando...")

def listar_contas(contas):
    for conta in contas:
        mensagem = f'''
Agência: {conta['agencia']}
C/C: {conta['numero_conta']}
Titular: {conta['usuario']['nome']}\n'''
        
        print ("-"*70)
        print (mensagem)

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
usuarios = []
AGENCIA = "0001"
contas = []
numero_conta = 1

menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Usuário
[5] Nova Conta
[6] Listar Usuários
[7] Listar Contas
[8] Sair

=> """

while True:

    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = sacar(saldo = saldo, valor = valor,limite = limite, extrato = extrato, numero_saques = numero_saques, LIMITE_SAQUES = LIMITE_SAQUES)

    elif opcao == "3":
        mostrar_extrato(saldo, extrato = extrato)
    
    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        criar_conta(AGENCIA,numero_conta,usuarios,contas)
        numero_conta += 1

    elif opcao == "6":
        listar_usuarios(usuarios)
    
    elif opcao == "7":
        listar_contas(contas)

    elif opcao == "8":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")