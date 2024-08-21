def cliente():
    nome = input('Digite Seu nome: ')
    sobre_nome = input('Digite Seu sobrenome: ')
    return nome, sobre_nome

def deposito(saldo):
    valor_deposito = float(input('Digite o valor de depósito: '))
    saldo += valor_deposito
    print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso!")
    return saldo

def saque(saldo):
    valor_saque = float(input('Digite o valor do saque: '))
    LIMITE_SAQUES = 3
    saques_realizados = 0
    LIMITE_VALOR_SAQUE = 500.0

    if saques_realizados >= LIMITE_SAQUES:
        print("Limite de 3 saques por dia atingido.")
        return saldo, saques_realizados
    elif valor_saque > saldo:
        print("Saldo insuficiente para realizar o saque.")
    else:
        saldo -= valor_saque
        print(f"Saque de R${valor_saque:.2f} realizado com sucesso!")
    return saldo, saque

def extrato(saldo):
    print(f"Seu saldo atual é: R${saldo:.2f}")

def menu():
    nome, sobre_nome = cliente()
    print(f'Bem vindo {nome } {sobre_nome} ao banco da NTT')
    saldo = 0.0  # Saldo inicial

    while True:
        print("""
        ===================== MENU ===========================
        1. Depósito
        2. Saque
        3. Extrato
        4. Sair
        =======================================================
        """)
        
        opcao = input(f"{nome} {sobre_nome}, selecione a operação: ")

        if opcao == '1':
            saldo = deposito(saldo)
        elif opcao == '2':
            saldo = saque(saldo)
        elif opcao == '3':
            extrato(saldo)
        elif opcao == '4':
            print("Saindo do sistema. Obrigado por usar o banco!")
            break
        else:
            print("Opção inválida. Por favor, tente novamente.")

menu()
