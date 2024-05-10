def menu():
    menu = """\n

        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Novo Usuario
        [5] Listar Usuarios
        [6] Nova Conta
        [q] Sair

    => """

    return input(menu)


def depositar(saldo, valor, extrato, /):
    
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"

    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    
    excedeu_saldo = valor > saldo

    excedeu_limite = valor > limite

    excedeu_saques = numero_saques >= limite_saques

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


def novo_usuario(usuarios):

    cpf = input('Digite seu CPF: ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Ja existe usuario com esse cpf !')
        return
    
    nome = input('Digite seu nome: ')
    data_nascimento = input('Digite sua data de nascimento: ')
    endereco = input('Digite seu endereço: ')

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, 
                    "cpf": cpf, "endereco": endereco})

    print('Usuario criado com sucesso !')


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)


    if usuario:
        print("Conta criada com sucesso! ")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print(" Usuário não encontrado, fluxo de criação de conta encerrado!")    


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        print("=" * 100)
        print(linha)


def mostrar_extrato(saldo, /, *, extrato):

    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")



def main():

    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []


    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = (depositar(saldo, valor, extrato))


        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo = saldo, 
                valor = valor, 
                extrato = extrato,
                limite = limite,
                numero_saques = numero_saques,
                limite_saques = LIMITE_SAQUES,
                )
            

        elif opcao == "3":
            mostrar_extrato(saldo, extrato=extrato)


        elif opcao == "4":
            ...
             

        elif opcao == "5":
            ...
        

        elif opcao == "6":
            ...
        
        
        elif opcao == "q":
            ...


        

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

main()