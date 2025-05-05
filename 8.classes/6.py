import os
from dataclasses import dataclass

os.system("cls || clear")

@dataclass
class Paciente:
    nome: str
    idade: int

    def exibir_dados(self):
        print(f"Nome: {self.nome} \nidade: {self.idade}\n\n")

paciente1 = Paciente(nome="Marta", idade=45)

lista_pacientes = []
QUANTIDADE_PACIENTES = 2

for i in range(QUANTIDADE_PACIENTES):
    paciente = Paciente(
                    nome = input("Digite seu nome: ")
                    idade = int(input("Digite a idade: "))
                )
    lista_pacientes.append(paciente)

print("\nExibindo Dados do usuário.")
for paciente in lista_pessoas:
    paciente.exibir_dados()    