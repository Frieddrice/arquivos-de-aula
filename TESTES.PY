
import cabecalho_miniprojeto as d
d.limpa_tudo() #Limpa as informações antes do programa iniciar
d.cabecalho_de_todos() #Chama uma definição já feita que indica quem o programa

id = 0
contas = []

def cadastro(): #Definição que permite o cadastro
    global id
    id = id+10
    #deine números de id dos usuários, 
    saldo = 0
    print("\n-Efetue o cadastro-")
    nome = input("\nDigite o seu nome de usuário: ")
    pin = input("Digite o seu PIN: ")
    contas.append([nome,id,pin,saldo])
    print("\nUsuário cadastrado com sucesso! Seu ID é: ")
    print(id)#O programa informa o ID do usuário a partir 

def login(): #Definição que permite o login 
    print("\n-Efetue o login-") 
    id = input("\nInsira o seu ID: ")
    senha =input("Insira Senha: ")
    for u in contas:
        if str(u[1]) == id and u[2] == senha:
            print("\nSeu login foi efetuado com sucesso!")
            return True
        
        else:
            print("Conta ou senha inválidas, tente novamente.")
            return False

def operacoes():
    opcao=0
    saldo=0
    deposito=[]
    saque=[]
    transferencia=[]
    #Defino as variáveis do meu programa com valores
    
    while opcao<4: #Enquanto a variável "opção" for menor que 4, haverão as seguintes opções:
        print ("\nMENU DE OPÇÕES:")
        print ("Digite:")
        print ("1 para: Saldo")
        print ("2 para: Depósito")
        print ("3 para: Saque")
        print ("4 para: Transferência")
        print ("0 para: Encerrar sessão")
        opcao= int(input("Insira uma opção: "))
        #O programa irá apresentar as opções possíveis e irá solicitar a escolha do programador
        
        if opcao==1:
            print ("Seu saldo disponível é de: R$", saldo)
            print("\n")
        #Caso o programador tenha digitado 1, ele irá visualizar seu saldo inicial
        
        elif opcao==2:
            deposito= int (input("Digite o valor do depósito que deseja fazer: R$"))
            if deposito<=0:
                print("Não é possível depositar uma quantia negativa")
            else:
                saldo=saldo+deposito
                print ("O saldo atual é: ", saldo)
                print("\n")
        #Caso tenha digitado 2, o programa irá solicitar o valor do depósito e irá apresentar o novo saldo
        
        elif opcao==3:
            saque= int(input("Digite quanto deseja sacar: R$"))
            if saque<=0:
                print("Saldo insuficiente, não é possível realizar o saque.")
            if saque<saldo:
                print("Não é possível sacar uma quantia negativa.")
            else:
                saldo=saldo-saque
                print ("O saldo atual é de:", saldo)
                print("\n")
        #Caso tenha digitado 3, o programa irá solicitar o valor do saque e irá apresentar o novo saldo
        
        elif opcao==4:
            id_transf=int(input("Digite o ID da conta para transferência: "))
            transferencia=int(input("Digite o valor que deseja transferir: R$ "))
            if transferencia <= 0:
                print("Não é possível transferir valores negativos.")
            if transferencia > saldo:
                print ("Saldo insuficiente.")
            else:
                for u in contas:
                    if u[1] == id_transf:
                        saldo = saldo - transferencia
                        u[3] = u[3] + transferencia
                        print("Transferência feita com sucesso!")
                        print("Seu saldo atual é: R$", saldo)
                        break
                

                    
        #Caso o usuário tenha digitado 4, então ele terá que selecionar uma conta para qual será feita a transferência
        #O valor transferido irá retirado do saldo do usuário que deseja fazer a transferência, para o usuário que receberá o valor.
        
        elif opcao==0:
            print("Sessão encerrada, até mais!")
            break
        #Caso tenha digitado 0 e escolhido finalizar a sessão, o programa irá encerrar e mandar uma mensagem de despedida

        else:
            print("Opção inválida")
            break
        #Caso a opção digitada não corresponda às definidas, o programa irá indicar que a opção é inválida
        
while True:
    print("\n-- SISTEMA BANCÁRIO --")
    print("\n1 - Cadastrar")
    print("2 - Logar")
    print("3 - Listar contas")
    print("4 - Sair")
    #o programa define a função de cada número digitado 

    opcao=int(input("\nO que você deseja fazer? Digite uma opção: ")) #O programa pergunta ao usuário o que ele deseja
    if opcao==1:#Se a opção do usuário for =1, ele irá se cadastrar no sistema
        cadastro()
    
    elif opcao==2:
        if login():
            operacoes()
        #o código roda as funções 
    elif opcao==3:
        print(contas)

    elif opcao==4:
        print("\nEncerrando o sistema...")
        break 

    else:
        print("\nOpção inválida, tente novamente.")