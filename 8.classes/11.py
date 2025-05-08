import os 
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Funcionario:
    nome: str
    data_admissao: int
    matricula: int
    endereco: str
class Cliente:  
    nome: str
    data_nascimento: str
    endereco: str

    def exibir_resultados(self):
        print(f"\nNome: {self.nome} \nData de Admissao: {self.data_admissao}\nMatrcicula: {self.matricula} \nEndereço: {self.endereco}\n")