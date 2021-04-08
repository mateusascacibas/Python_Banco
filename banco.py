from typing import List
from time import sleep
from BancoPy.Models.conta import Conta
from BancoPy.Models.cliente import Cliente

contas: List[Conta] = []

def main() -> None:
    menu()

def menu() -> None:
    print("======================")
    print("======= ATM ==========")
    print("Mateus Bank")
    print("======================")

    print("Selecione uma opção no Menu")
    print("1 - Criar conta")
    print("2 - Efetuar saque")
    print("3 - Efetuar deposito")
    print("4 - Efetuar transferencia")
    print("5 - Listar contas")
    print("6 - Sair do sistema")

    opcao: int = (int(input()))

    if opcao == 1:
        criar_conta()
    elif opcao == 2:
        efetuar_saque()
    elif opcao == 3:
        efetuar_deposito()
    elif opcao == 4:
        efetuar_transferencia()
    elif opcao == 5:
        listar_contas()
    elif opcao == 6:
        print("Volte sempre!")
        sleep(2)
        exit()
    else:
        print("Opcão invalida.")
        sleep(2)
        menu()

def criar_conta() -> None:
    print("Informe os dados do cliente: ")
    nome: str = input("Nome do cliente: ")
    email: str = input("Email do cliente: ")
    cpf: str = input("CPF do cliente: ")
    data_nascimento: str = input("Data de nascimento do cliente: ")
    cliente: Cliente = Cliente(nome, email, cpf, data_nascimento)
    conta: Conta = Conta(cliente)

    contas.append(conta)

    print("Conta criada com sucesso.")
    print("Dados da conta: ")
    print("===============")
    print(Conta)
    sleep(2)
    menu()

def efetuar_saque() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor do saque: "))

            conta.sacar(valor)

        else:
            print(f"A conta com o numero {numero} não foi encontrada.")
    else:
        print("Não existem contas cadastradas")
    sleep(2)
    menu()

def efetuar_deposito() -> None:
    if len(contas) > 0:
        numero: int = int(input("Informe o numero da sua conta: "))
        conta: Conta = buscar_conta_por_numero(numero)
        if conta:
            valor: float = float(input("Informe o valor do deposito: "))

            conta.depositar(valor)

        else:
            print(f"A conta com o numero {numero} não foi encontrada.")
    else:
        print("Não existem contas cadastradas")
    sleep(2)
    menu()


def efetuar_transferencia() -> None:
    if len(contas) > 0:
        numero_o: int = int(input("Informe o numero da sua conta: "))
        conta_o: Conta = buscar_conta_por_numero(numero_o)

        if conta_o:
            numero_d: int = int(input("Informe o numero da conta destino: "))
            conta_d: Conta = buscar_conta_por_numero(numero_d)

            if conta_d:
                valor: float = float(input("Informe o valor da transferencia: "))
                conta_o.transferir(conta_d, valor)
            else:
                print(f"A conta destino com o numero {numero_d} não foi encontrada.")
        else:
            print(f'A conta com o numero {numero_o} não foi encontrada.')
    else:
        print("Não existem contas cadastradas")
    sleep(2)
    menu()

def listar_contas() -> None:
    if len(contas) > 0:
        print("Listagem de contas")
        for conta in contas:
            print(conta)
            print("==========")
            sleep(1)
    else:
        print("Não existem contas cadastradas")
    sleep(2)
    menu()


def buscar_conta_por_numero(numero: int) -> Conta:
    c: Conta = None

    if len(contas) > 0:
        for conta in contas:
            if conta.numero == numero:
                c = conta
    return c

if __name__ == '__main__':
    main()