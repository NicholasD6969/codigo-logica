import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Pesssoa:
    nome: str
    idade: int
    Peso: float
    altura: float

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nidade: {self.idade} Peso: {self.Peso} Altura: {self.altura}\n\n\n\n")

lista_pessoas = []
QUANTIDADE_PESSOAS = 4

for i in range(QUANTIDADE_PESSOAS):
    pesssoa = Pesssoa(
        nome = input("Digite o nome: "),
        idade = int(input("Digite a idade: ")),
        Peso = float(input("Digite o peso: ")),
        altura = float(input("Digite a altura"))
                    )
    lista_pessoas.append(pesssoa)

print("\nExibindo Dados do usuário.")
for pessoa in lista_pessoas:
    pessoa.exibir_dados()   