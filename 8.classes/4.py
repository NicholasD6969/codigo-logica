import os 
os.system("cla || clear")
from dataclasses import dataclass

@dataclass
class Endereço:
    logradouro: str
    numero: str

@dataclass
class Pessoa:
    nome: str
    idade: int
    endereço: Endereço # classe endereço

    def exibir_dados(self):
        print(f"Nome: {self.nome}, idade: {self.idade}, Logradouro: {self.endereço.logradouro}, Numero: {self.endereço.numero}")

Endereço = Endereço("Rua Da Paz", "a-0")
Pessoa = Pessoa("Nicholas", 17, Endereço)

print("Dados Da Pessoas: ")
Pessoa.exibir_dados()