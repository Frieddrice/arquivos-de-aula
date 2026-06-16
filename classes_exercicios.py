import definicoes as d
d.limpa()
d.cabecalho()
#2. Classe Quadrado
#Atributo: Tamanho do lado
#Métodos: mudarLado, mostrarLado, calcularArea
class Quadrado():
    def __init__(self,lado):
        self.lado = lado
    def mudarLado(self,novolado):
        self.lado = novolado
        self.mostrarLado()
    def mostrarLado(self):
        print(f"O tamanho do lado é: {self.lado}")
    def calcularArea(self):
        area = self.lado*self.lado
        print (f"A área é: {area}\n")
quadrado1 = Quadrado(5)
quadrado1.mostrarLado()
quadrado1.mudarLado(8)
quadrado1.calcularArea()

#3. Classe Pessoa
#Atributos: nome, idade, peso, altura
#Métodos: envelhecer, engordar, emagrecer, crescer
class Pessoa():

    def __init__(self,nome,idade,peso,altura):
        self.nome = nome
        self.idade = idade 
        self.peso = peso
        self.altura = altura
        self.Vida()

    def Envelhecer (self,novaidade):
        if novaidade < 1 :
            print("Envelhecimento não permitido")
        else:
            self.idade += novaidade

    def Engordar (self,ganhapeso):
        if ganhapeso < 1 :
            print("Engordar não foi permitido")
        else:
            self.peso += ganhapeso

    def Emagrecer (self,perdepeso):
         if perdepeso < 1 :
            print("Emagrecimento não permitido")
         else:
             self.peso -= perdepeso
    
    def Crescer (self,novaaltura):
        if novaaltura < 1 :
            print("Crescimento não permitido")
        else:
             self.altura += novaaltura
    
    def Vida (self):
        print(f"{self.nome} possui {self.idade} e {self.altura} de altura\n")
    
melyssa = Pessoa("Melyssa",16,55,1.57)
melyssa.Envelhecer(4)
melyssa.Engordar (5)
melyssa.Emagrecer(10)
melyssa.Crescer(3)
melyssa.Vida()


#4. Classe Conta Corrente
#Atributos: número da conta, nome do correntista, saldo (defalt = 0)
#Métodos: AlterarNome, depositar, sacar
class Conta_Corrente():
    saldo = 0
    def __init__(self,num_da_conta,nome):
            self.num_da_conta = num_da_conta
            self.nome = nome

    def alterarNome(self,novo_nome):
            self.nome = novo_nome

    def depositar(self,deposito):
        if deposito < 0:
            print("Depósito inválido")
        else:
            self.saldo += deposito

    def sacar(self,saque):
        if saque <0:
            print("Saque inválido")
        else:
            self.saldo -= saque
    
