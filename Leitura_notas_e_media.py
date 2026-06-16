import definicoes as d
d.limpa()
d.cabecalho()
inicio = input("Digite 4 notas: ")
num1 = int(input("Primeira nota: "))
num2 = int(input("Segunda nota: "))
num3 = int(input("Terceiro número: "))
num4 = int(input("Quarto número: "))
lista = [num1,num2,num3,num4]
print("Suas notas são:",lista)
media = (num1+num2+num3+num4)/4
print("Sua média é:",media)