#Leia um vetor de 5 números inteiros. Mostre a soma, a multiplicação e os números
import definicoes as d
d.limpa()
d.cabecalho()

inicio = input("Digite 5 números inteiros: ")
num1 = int(input("Primeiro número: "))
num2 = int(input("Segundo número: "))
num3 = int(input("Terceiro número: "))
num4 = int(input("Quarto número: "))
num5 = int(input("Quinto número: "))
lista = [num1,num2,num3,num4,num5]
print("Os 5 números digitados são", lista)
soma = num1+num2+num3+num4+num5
print("A soma de todos os números é de:",soma)
multip= num1*num2*num3*num4*num5
print("A multiplicação de todos os números é de:",multip)
