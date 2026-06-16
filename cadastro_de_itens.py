import definicoes as d
d.limpa()
d.cabecalho()
import csv
from statistics import quantiles 
"""with open('estoque.csv',w,encoding='utf-8') as estoque:
    escritor = csv.writer(estoque)
    escritor.writerow(['nome','preco','quantidade'])"""

estrutura = ['nome','preco','quantidade']
def cadastro_produto(nome,preco,quantidade): #Argumentos (o que o objeto deve conter)
    with open('estoque.csv','a',newline='')as estoque:
        produto = {'nome':nome,'preco':preco,'quantidade':quantidade}
        escritor = csv.DictWriter(estoque,fieldnames = estrutura) #fieldnames (como se fosse a coluna do excel, que seria tipo a posição de cada argumento)
        escritor.writerow(produto) #Writerow (Utilizado para simplificar a escrita na hora de produzir uma sequência, sem necessidade da vírgula)

def listar_produtos():
    with open('estoque.csv','r') as estoque:
        leitor= csv.DictReader(estoque)
        for itens in leitor: 
            print(f"Nome: {itens['nome']} | Preço: {itens['preco']} | Quantidade: {itens['quantidade']}")

def modificar_preco(nome,novo_preco):
    produtos = []
    with open('estoque.csv',"r", newline='') as estoque:
        leitor = csv.DictReader(estoque)
        for produto in leitor: 
            if produto ['nome'] == nome:
               produto['preco'] == novo_preco
            produtos.append(produto)
    with open('estoque.csv','w', newline='', encoding='utf-8') as estoque:
                escritor = csv.DictWriter(estoque, fieldnames=estrutura)
                escritor.writeheader()
                escritor.writerows(produtos)
modificar_preco('Pipoca Doce', 10)


