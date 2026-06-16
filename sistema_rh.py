import definicoes as d
d.limpa()
d.cabecalho()
class Funcionario():
    def __init__(self,nome,cpf,salariobruto):
        self.nome = nome
        self.cpf = cpf
        if salariobruto <1621:
            print("Salário menor do que o mínimo")
            return
        else:
            self.salariobruto = salariobruto

    def infoFuncionario(self):
        salarioliquido = self.salarioLiquido()
        print(f"Nome: {self.nome}")
        print(f"CPF: {self.cpf}")
        print(f"Salário Bruto: {self.salariobruto}")
        print(f"Salário Líquido: {salarioliquido}")

    def salarioLiquido(self):
        #Desconto IR
        if self.salariobruto<=5000:
            desconto_ir = 0
        elif self.salariobruto <=7500:
            desconto_ir= self.salariobruto*0.075
        elif self.salariobruto<=8000:
            desconto_ir= self.saldobruto*0.15
        elif self.salariobruto <=9500:
            desconto_ir= self.salariobruto*0.225
        else: 
            desconto_ir = self.salariobruto*0.275

        #Desconto INSS
        if self.salariobruto <= 1621:
            desconto_inss = self.salariobruto*0.075
        elif self.salariobruto <=3000:
            desconto_inss = self.salariobruto*0.09
        elif self.salariobruto <= 5000:
            desconto_inss = self.salariobruto*0.12
        else:
            desconto_inss = self.salariobruto*0.14
        salarioliquido = self.salariobruto - (desconto_inss + desconto_ir)
        return salarioliquido
    
    def receberAumento(self,percentual):
        self.salariobruto = self.salariobruto + self.salariobruto*(percentual/100) #Salário antigo + SalárioAntigo"Percentual dividido por 100
        self.salarioliquido()

Funcionario1= Funcionario("Sophia", 111111111-11,1621)
Funcionario2=Funcionario("Ana Luiza", 555555555-55, 5000)

Funcionario1.infoFuncionario()
Funcionario2.infoFuncionario()






