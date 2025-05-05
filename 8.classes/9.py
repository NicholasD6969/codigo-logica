import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Autor:
    nome: str
    biografia: str

class Livro:
    titulo: str
    ano: int

    def exibir_detalhes(self):
        print(f"\nTitulo: {self.titulo} \nAno: {self.ano}")

