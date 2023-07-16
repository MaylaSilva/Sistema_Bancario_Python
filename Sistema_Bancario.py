menu = """

(1) depositar
(2) sacar
(3) extrato
(4) sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print ("Depósito")
        valor_depositado = float(input("Digite quanto deseja depositar: "))
        if valor_depositado > 0:
            saldo += valor_depositado
            extrato += f"Depósito de R$ {valor_depositado: .2f}\n"
            print (f"Seu saldo é: R$ {saldo: .2f}")
        else:
            print ("Valor inválido! Repita a operação.")
    
    elif opcao == "2":
        print ("Saque")
        valor_sacado = float(input ("Digite o valor a ser sacado: "))
        excedeu_saldo = valor_sacado > saldo
        excedeu_limite = valor_sacado > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUE

        if excedeu_saldo:
            print ("Saldo insuficiente")
        elif excedeu_limite:
            print ("Valor de saque excedido")
        elif excedeu_saques:
            print ("Quantidade diária de saque excedida")
        
        elif valor_sacado > 0:
                saldo -= valor_sacado
                extrato += f"Saque de R$ {valor_sacado: .2f} \n"
                numero_saques += 1
        else: print ("Valor informado inválido")
        print (f"Seu saldo é: R$ {saldo: .2f}")    
    
    elif opcao == "3":
        print ("-------------------EXTRATO-------------------\n")
        print (f"{extrato}\nSeu saldo é de R$ {saldo: .2f}")

    elif opcao == "4":
        break
    
    else: print ("Opção inválida, por favor selecione novamente a opção desejada.")
