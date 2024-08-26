from colorama import init, Fore, Style
import textwrap

init(autoreset=True)


class UsuarioJaCadastradoError(Exception):
    """Exceção levantada quando o usuário já está cadastrado."""

    pass


def menu():
    menu = (
        Fore.WHITE
        + Style.BRIGHT
        + """\n
    ================ MENU =========================
    [1]\tDepositar
    [2]\tSacar
    [3]\tExtrato
    [4]\tNova conta
    [5]\tLista contas
    [6]\tNovo usuário
    [7]\tSair
    =>
    """
    )
    return input(textwrap.dedent(menu))


def depositar(saldo, valor, extrato, /):
    try:

        valor = valor
        if valor > 0:
            saldo += valor
            extrato += f"\t\tDepósito: R$ {valor:.2f}\n"
            print(Fore.GREEN + Style.BRIGHT + "\nDepósito realizado com sucesso!")
        else:
            print(
                Fore.RED
                + Style.BRIGHT
                + "\nOperação falhou! O valor informado é inválido."
            )
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"\nErro inesperado: {e}")

    return saldo, extrato


def sacar(
    *, saldo, valor, extrato, limite, numeros_saques, limite_saques, total_saques
):

    try:
        if valor < 0:
            print(
                Fore.RED
                + Style.BRIGHT
                + "\nOperação falhou! Saldo da conta está negativo. Corrija o saldo antes de realizar saques."
            )
        elif numeros_saques >= limite_saques:
            print(
                Fore.RED
                + Style.BRIGHT
                + "\nOperação falhou! Limite de Saquer diario excedido."
            )
        elif valor >= limite or total_saques + valor >= limite:
            print(
                Fore.RED
                + Style.BRIGHT
                + f"\nOperação falhou! O limite de saque é R$ {limite:.2f}."
            )
        elif saldo <= valor:
            print(Fore.RED + Style.BRIGHT + f"\nOperação falhou! Saldo insuficiente.")
        else:
            saldo -= valor
            total_saques += valor
            numeros_saques += 1
            extrato += f"\t\tSaque: R$ {valor:.2f}\n"
            print(Fore.GREEN + Style.BRIGHT + "\nSaque realizado com sucesso!")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"\nErro inesperado: {e}")

    return saldo, extrato, numeros_saques, total_saques


def exibir_extrato(saldo, /, *, extrato):
    print()
    print(
        Fore.WHITE
        + Style.BRIGHT
        + f"""
        \n================ EXTRATO =========================\n
        \tSeu saldo atual é {saldo}
        \n==================================================\n
        \tSuas Trançaçoes atuais:
        """
    )
    if extrato:
        print(Fore.WHITE + Style.BRIGHT + extrato)
        print("\n================================================\n")
    else:
        print(Fore.YELLOW + Style.BRIGHT + "\t\tNenhuma transação registrada.")


def criar_usuario(usuarios):
    try:
        cpf = input("Informe o CPF somente números: ")

        if not validar_cpf(cpf):
            raise ValueError(
                "CPF inválido. Certifique-se de que o CPF tem 11 dígitos numéricos."
            )

        usuario_existente = filtrar_usuario(cpf, usuarios)
        if usuario_existente:
            raise UsuarioJaCadastradoError("Usuário já está cadastrado.")

        nome = input("Informe o nome completo: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/aaaa): ")

        usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf})
        print(f"Usuário {nome} adicionado com sucesso!")

    except ValueError as e:
        print(Fore.RED + Style.BRIGHT + f"Erro: {e}")

    except UsuarioJaCadastradoError as e:
        print(Fore.RED + Style.BRIGHT + f"Erro: {e}")

    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"Erro inesperado: {e}")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    try:
        cpf = input("Informe o CPF usuario: ")
        usuarios = filtrar_usuario(cpf, usuarios)
        
        if usuarios:
            print("\t\t Conta criada com sucesso!")
            return {"agencia": agencia, "numero_conta": numero_conta, "usuarios": usuarios}
    except ValueError as e:
        print(Fore.RED + Style.BRIGHT + f"Erro: {e}")
    except Exception as e:
        print(Fore.RED + Style.BRIGHT + f"Erro inesperado: {e}")


def lista_contas(contas):
    for contas in contas:
        print( Fore.WHITE
        + Style.BRIGHT + f"""
        ================== SUES DADOS BANCARIOS ===========================\n
        \t\tConta: {contas['numero_conta']} 
        \t\tAgência: {contas['agencia']}
        \t\tUsuário: {contas['usuarios']['nome']}
        \n
        =============================================== """)


def validar_cpf(cpf):
    cpf = "".join(filter(str.isdigit, cpf))
    return len(cpf) == 11


def main():
    LIMITE_SAQUE = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numeros_saques = 0
    usuarios = []
    contas = []
    total_saques = 0.0

    while True:
        opcao = menu()
        if opcao == "1":
            while True:
                try:
                    valor = float(
                        input(
                            Fore.WHITE
                            + Style.BRIGHT
                            + "\nInforme o valor do depósito: "
                        )
                    )
                    break  # encerramento do tratamento de valor
                except ValueError:
                    print(
                        Fore.RED
                        + Style.BRIGHT
                        + "\nErro: Entrada inválida! Por favor, insira um número válido."
                    )

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2":
            while True:
                try:
                    valor = float(
                        input(
                            Fore.GREEN + Style.BRIGHT + "\nInforme o valor do saque: "
                        )
                    )
                    break
                except ValueError:
                    print(
                        Fore.RED
                        + Style.BRIGHT
                        + "\nErro: Entrada inválida! Por favor, insira um número válido."
                    )

            saldo, extrato, numeros_saques, total_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numeros_saques=numeros_saques,
                limite_saques=LIMITE_SAQUE,
                total_saques=total_saques,
            )

        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "6":
            criar_usuario(usuarios)

        elif opcao == "5":
            lista_contas(contas)

        elif opcao == "4":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "7":
            break


main()
