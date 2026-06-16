import definicoes as d
d.limpa()
d.cabecalho()

lista=[]
pares=[]
impares=[]
for i in range(0, 20):
    m= int(input(f"Digite o {i+1}° valor: "))
    lista.append(m)
    if m % 2 == 0: 
        pares.append(m)
    else: 
        impares.append(m)

print("Os números da lista são:",lista)
print("Os números pares são",pares)
print("Os números ímpares são",impares)