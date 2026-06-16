import definicoes as d
d.limpa()
d.cabecalho()
class Pessoa ():
    #Característica fixas:
    olhos = 2
    queixo = 1
    #Características do CONSTRUIDOR DE CLASSES:
    def __init__(self,altura):
        self.altura = altura

melyssa = Pessoa(157)
sophia = Pessoa(165)


