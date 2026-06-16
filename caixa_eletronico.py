import definicoes as d
d.limpa()
d.cabecalho()
saldo = 100
opcao = 0
while opcao <4: 
    print("Menu inicial:")
    print("1 - Visualizar saldo")
    print("2 - Depósito")
    print("3 - Saque")
    print("4 - Encerrar")
    opcao = int(input("\nDigite o número correspondente ao que deseja fazer: "))
    if opcao == 1:
        print("\nSaldo")
        print("O seu saldo atual é de:R$",saldo,"\n")
    elif opcao == 2:
        print("Depósito")
        deposito = int(input("Informe o depósito que deseja fazer: "))
        saldo = saldo+deposito
        print("Seu depósito é de:R$",deposito,"e o seu saldo, com o depósito adicionado é de: R$",saldo,"\n")
    elif opcao == 3:
        print("\nSaque")
        saque = int(input("Informe o saque que deseja efetuar: "))
        saldo= saldo-saque
        print("O seu saldo final é de:R$",saldo,"\n")
    elif opcao == 4:
        print("Serviço finalizado")
    else: 
        print("Opção inválida.")
        break