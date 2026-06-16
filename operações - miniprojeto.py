import definicoes as d
d.limpa() 
d.cabecalho() 

def operacoes():
    opcao=0
    saldo=0
    deposito=[]
    saque=[]
    tranferencia=[]


    while opcao<4:
        print ("\nMENU DE OPÇÕES:")
        print ("Digite:")
        print ("1 para: Saldo")
        print ("2 para: Depósito")
        print ("3 para: Saque")
        print ("4 para: Transferência")
        print ("0 para: Encerrar sessão")
        opcao= int(input("Insira uma opção: "))
        

        if opcao==1:
            print ("Seu saldo disponível é de: R$", saldo)
            print("\n")
            

        
        elif opcao==2:
            deposito= int (input("Digite o valor do depósito que deseja fazer: R$"))
            saldo=saldo+deposito
            print ("O saldo atual é: ", saldo)
            print("\n")
            
        
        elif opcao==3:
            saque= int(input("Digite quanto deseja sacar: R$"))
            if saque>saldo:
                print("Saldo insuficiente, não é possível realizar o saque.")
            else:
                saldo=saldo-saque
                print ("O saldo atual é de:", saldo)
                print("\n")
        

        elif opcao==4:
            id=input("Digite a conta a ser transferida: ")
            for u in contas:
                if u[1]==id:
                    saldo-=tranferencia
                    u[3]+=tranferencia


        elif opcao==0:
            print("Sessão encerrada, até mais!")
            break
        
        else:
            print("Opção inválida")
            break
    
  
   