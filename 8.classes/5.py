import os 
os.system("cla || clear")
from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    email: str

@dataclass
class endereco:
    logradouro: str
    numero: int
    cidade: str

    def exibir_dados(self):
        print(f"Nome: {self.nome}, E-mail: {self.email}, Logradouro: {self.endereco.logradouro}, numero: {self.endereco.numero}, cidade: {self.endereco.cidade}") 

nome = input("Digite o nome: ")
email = input("Digite o Email: ")    
logradouro = input("Digite o Logradouro: ")    
numero = int(input("Digite o Numero: "))
cidade = input("Digite a cidade: ")    


pessoa1 = pessoa(nome=nome, email=email)
endereco1 = endereco(logradouro=logradouro, numero=numero, cidade=cidade )

print("\nDados Pessoas: ")

pessoa1.exibir_dados()