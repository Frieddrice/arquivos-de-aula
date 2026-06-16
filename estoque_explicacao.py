import csv

campos = ['nome_do_produto','quantidade','preco']
try:
    with open('armazenamento.csv','r') as armazenamento:
        print("Arquivo existente")
except FileNotFoundError:
    print("Criando arquivo")
    with open('armazenamento.csv', 'w',newline='') as armazenamento:
        escritor = csv.DictWriter(armazenamento,fieldnames=campos)
        escritor.writeheader()
    print("Arquivo criado")

def cadastrar(A,B,C):
        produto = {'nome_do_produto': A, 'quantidade':B, 'preco':C}
        with open('armazenamento.csv','a',newline='') as armazenamento:
            escritor = csv.DictWriter(armazenamento,fieldnames=campos)
            escritor.writerow(produto)
def remover(nome):
    lista_de_produtos = []
    with open('armazenamento.csv', 'r') as estoque:
         leitor = csv.DictReader(armazenamento)
         for item in leitor:
            if item['nome_do_produto'] != nome:
              lista_de_produtos.append(item)
    with open('armazenamento.csv', 'w',newline='') as armazenamento:
        escritor = csv.DictWriter(armazenamento,fieldnames=campos)
        escritor.writeheader()
        for itens in lista_de_produtos:
            escritor.writerow(itens)
def modificar(nome,novo_preco):
    lista_de_produtos = []
    with open('armazenamento.csv','r') as armazenamento:
        leitor = csv.DictReader(armazenamento)
        for item in leitor:
            if item['nome_do_produto'] == nome:
                item['preco'] = novo_preco
            lista_de_produtos.append(item)
    with open ('estoques.csv','w',newline='')as armazem:
        escritor = csv.DictWriter(armazem,fieldnames=campos)
        escritor.writeheader()
        for itens in lista_de_produtos:
            escritor.writerow(itens)