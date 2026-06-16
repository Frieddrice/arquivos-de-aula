import cabecalho_miniprojeto as d
d.limpa_tudo() #Limpa as informações antes do programa iniciar
d.cabecalho_de_todos() #Chama uma definição já feita que indica quem o programa

id = 0
contas = []

print("\n-- SISTEMA BANCÁRIO --")
print("\n1 - Cadastrar")
print("2 - Logar")
print("3 - Listar contas")
print("4 - Sair")

opcao=int(input("\nO que você deseja fazer? Digite uma opção: ")) #O programa pergunta ao usuário o que ele deseja

case 1:
cadastro()
case2:
login()

def cadastro():
    global id
    id = id+10
    saldo = 0
    nome = input("Digite o seu nome de usuário: ")
    pin = input("Digite o seu PIN: ")
    contas.append([id,nome,pin,saldo])
    print("Usuário cadastrado com sucesso.")