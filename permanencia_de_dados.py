import definicoes as d
d.limpa()
d.cabecalho()
#Escrever dados em txt
#Quando quero que o arquivo seja apenas para leitura, utilizamos o modo leitura ---> r (de read)
#Quando o arquivo for editável (ler e escrever), utilizamos w (write)
#Quando quero adicionar ---> a
import csv
with open('turma.csv','r',encoding='utf-8') as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        if linha ['nome']== "Bruno":
            print(f"Nota do Bruno é: {linha['nota']}")


#lista com nome, notas e turma de alunos
while True: #Enquanto verdade for verdade
    print("1 - Cadastro")
    print ("2 - Listar alunos")
    opcao = int(input("Digite sua opção: "))

    if opcao == 1:
        nome = input("Digite seu nome: ")
        nota = input ("Digite a sua nota: ")
        turma = input ("Digite sua turma: ")
        with open('turma.csv','a',newline='',encoding='utf-8') as f:
    elif opcao == 2:
        print (alunos)
    else:
        break






