menu="""
============= MENU =============

1 - Depositar
2 - Sacar
3 - Visualizar Extrato
0 - Sair

================================
"""

saldo = 0
limite = 500
count_saque = 0

saques = []
depositos = []

#---------------------------------------------------------------------------
def main():
#---------------------------------------------------------------------------
    while True:
        print(menu)

        opcao = int(input("Digite o número do menu que deseja acessar: "))

        if opcao == 1:
            depositar()
        elif opcao == 2:
            sacar()
        elif opcao == 3:
            visualizar_extrato()
        elif opcao == 0:
            break
        else:
            print("Número inválido. Digite outro número para continuar...")

#---------------------------------------------------------------------------
def sacar():
#---------------------------------------------------------------------------
    global count_saque
    global saldo
    global limite
    global saques

    valor = float(input("Digite o valor que deseja sacar: "))

    if count_saque >= 3:
        print("Você já realizou 3 saques hoje. Tente novamente amanhã!")
    elif (saldo <= 0) or (valor > saldo):
        print(f"Seu saldo é de R$ {saldo:.2f}. Não é possivel realizar o saque!")
    elif valor > limite:
        print(f"Não foi possivel realizar a transação. Limite de saque R$ {limite:.2f}.")
    else:
        saldo -= valor
        saques.append(f'- R$ {valor:.2f}')
        count_saque += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo Atual: {saldo:.2f}")

#---------------------------------------------------------------------------
def depositar():
#---------------------------------------------------------------------------
    global count_saque
    global saldo
    global depositos

    valor = float(input("Digite o valor que deseja depositar: "))
    
    if valor <= 0:
        print("Você digitou um valor inválido! Digite valores acima de R$ 0,00")
    else:
        saldo += valor
        depositos.append(f'+ R$ {valor:.2f}')
        print(f"Deposito de R$ {valor:.2f} realizado com sucesso!")
        print(f"Saldo Atual: {saldo:.2f}")


#---------------------------------------------------------------------------
def visualizar_extrato():
#---------------------------------------------------------------------------
    global saldo
    global saques
    global depositos

    if saques or depositos: 
        print("=" * 40)
        print("EXTRATO".center(40))
        print("=" * 40)

        for deposito in depositos:
            print(f"DEPÓSITO: {deposito.rjust(30)}")  

        for saque in saques:
            print(f"SAQUE:    {saque.rjust(30)}")

        print("=" * 40)
        print(f"SALDO:    {f'R$ {saldo:.2f}'.rjust(30)}")
        print("=" * 40)

    else:
        print("Não foram realizadas movimentações!")


#---------------------------------INICIO--------------------------------
if __name__ == "__main__":
    main()