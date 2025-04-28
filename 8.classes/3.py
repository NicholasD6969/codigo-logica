import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Login:
    nome: str
    email: str
    telefone: int
    endereço: str
    def exibindo_dados(self):
        print("\nExibindo dados: ")
        print(f"Nome: {self.nome}, e-mail: {self.email}, telefone: {self.telefone}, endereço: {self.endereço}")
nome =  input("Digite o nome: ")
email = str(input("Digite o email: "))
telefone = int(input("Digite o telefone: "))
endereço = str(input("Digite o endereço: "))

Login = Login (nome, email, telefone, endereço)
Login.exibindo_dados()