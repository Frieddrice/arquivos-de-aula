import definicoes as d
d.limpa()
lista = [1,2,3,4,5,6]
print(lista)
lista.append(2)
print(lista)
lista.remove(1)
lista.remove(4)
lista.append(2)
print(lista)
print(lista.count(2))