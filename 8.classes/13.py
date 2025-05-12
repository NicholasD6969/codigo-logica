import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Funcionarios:
    nome: str
    data: str
    cpf: int
    funcao: str

    def exibitr_dados(self):
        print(f"\nNome: {self.nome} \nData de Nascimento: {self.data} \nCpf:  {self.cpf} \nFunção: {self.funcao}")
lista_funcionarios = []
QUANTIDADE_FUNCIONARIOS = 2

for i in range (QUANTIDADE_FUNCIONARIOS):
    funcionarios = Funcionarios(
        nome = input("Digite o nome do funcionario: "),
        data = input("Digite a data de nascimento do funcionaruio: "),
        cpf = int(input("Digite o cpf do funcionario(somente numeros): ")),
        funcao = input("Qual função deste funcionario: "))

lista_funcionarios.append(funcionarios)
nome_arquivo = "funcionarios2_txt"
with open (nome_arquivo, "w") as arquivo_funcionario:
    for funcionarios in lista_funcionarios:
        arquivo_funcionario.write(f"\nNome:{funcionarios.nome} \nData de Nascimento: {funcionarios.data} \nCpf: {funcionarios.cpf} \nFunção: {funcionarios.funcao}")

print(".")

try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        dados = arquivo.readlines()
        for dado in dados:
            print(f"{dado.strip()}")
except FileNotFoundError:
    print("Arquivo não encontrado")         