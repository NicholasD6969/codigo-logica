import os
from dataclasses import dataclass
os.system("cls || clear")

@dataclass
class Livros:
    nome: str
    autor: str
    categoria: str
    preco: float

def exibir_dados(self):
        print(f"Nome: {self.nome} \nAutor: {self.autor} Categoria: {self.categoria} Preço: {self.preco}\n\n\n\n")

lista_livros = []
QUANTIDADE_LIVROS = 3

for i in range(QUANTIDADE_LIVROS):
    livro = Livros (
        
    )