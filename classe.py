import definicoes as d
d.limpa()
d.cabecalho()
class Pessoa ():
    #Característica fixas:
    olhos = 2
    queixo = 1
    altura = 170
    #Características do CONSTRUIDOR DE CLASSES:

lucas_lodi = Pessoa()
caua_lopes = Pessoa()
lucas_lodi.altura = 175
print(lucas_lodi.altura) #Objeto. (o ponto significa que eu solicito algo dentro da classe)
