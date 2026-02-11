class Cpf: 
    def __init__(self,nome,numero):
        self.nome = nome
        self.numero = numero

    def status(self):
        return f"{self.nome} e {self.numero}"


aluno = Cpf("Aluno1", 5015856)

print (f"{aluno.status()}")


class Gato:
    def __init__(self,nome,cor):
        self.nome =nome

    def falar(self):
        return f"Miau"

    def comer(self):
        return f"Comeu ração"

    def dormi(self):
        return f"Dormiu"

meu_gato = Gato("Garfield","Laranja")

print(f"Meu gato chama{meu_gato.falar()}")
print(f"Meu gato comeu? {meu_gato.comer()}")

class Veiculo:
    def __init__(self,modelo,cor,ano):
        self.modelo = modelo
        self.cor = cor
        self.ano = ano

veiculo1=Veiculo("Carro","Masda",1980)
veiculo2=Veiculo("moto", "ninja", 2007)

print(f"{veiculo1.modelo}")
print(f"{veiculo1.cor}")
print(f"{veiculo1.ano}")
print(f"{veiculo2.modelo}")
print(f"{veiculo2.cor}")
print(f"{veiculo2.ano}")

class Objeto:
    def __init__(self,modelo):
        self.modelo =modelo

lado1 =Objeto("quadrado,4")
lado2 =Objeto("quadrado2,4")

print(f"{lado1.modelo}")
print(f"{lado2.modelo}")