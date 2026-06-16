import definicoes as d
d.limpa()
d.cabecalho()
#Classe Bola
#Atribuos: Cor, circunferência, material
#métodos: trocaCor, mostraCor

class Bola():
    def __init__(self,cor,circunferencia,material):
         self.cor = cor
         self.circunferencia = circunferencia
         self.material = material
    def mostraCor(self):
         print(f"A bola de {self.material} com {self.circunferencia} cm posui cor: {self.cor}")    
    def trocaCor(self,nova_cor):
         self.cor = nova_cor