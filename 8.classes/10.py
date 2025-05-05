import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Pessoas:
    nome: str
    data: str
    rg: int
    cpf: int
    
    def solicitar_dados(self):
        print(f"\nNome: {self.nome} \nData de Nascimento: {self.data} \nRG: {self.rg} \nCPF: {self.cpf}")

lista_pessoas = []
QUANTIDADE_PESSOAS = 2

for i in range (QUANTIDADE_PESSOAS):
    pessoa = Pessoas(
        nome = input("Digite o nome do usuario: "),
        data = str(input("Digite a data de nascimento do usuario: ")),
        rg = int(input("Digite o RG do usuario: ")),
        cpf = int(input("Digite o CPF do usuario: "))
    )       
lista_pessoas.append(pessoa)
nome_arquivo = "funcionarios.txt"
with open (nome_arquivo, "w") as arquivo_pessoa:
    for pessoa in lista_pessoas:
        arquivo_pessoa.write(f"{pessoa.nome}\n{pessoa.data}\n{pessoa.rg}\n{pessoa.cpf}\n")

print("\nexibindo dados") 

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = arquivo.readlines()
        for dado in dados:
            print(f"{dado.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")            

