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
QUANTIDADE_LIVROS = 2

for i in range(QUANTIDADE_LIVROS):
    livro = Livros (
            nome = input("Digite o nome do Livro: "),
            autor = input("Digite o autor do livro: "),
            categoria = input("Digite a categoria do livro: "),
            preco = float(input("Digite o preço do livro: "))
    )
    lista_livros.append(livro)

nome_arquivo = "Dados_livros.txt"
with open(nome_arquivo, "a") as arquivo:
    for livro in lista_livros:
        arquivo.write(f"Nome: {livro.nome}, Autor: {livro.autor}, Categoria: {livro.categoria}, Preço: {livro.preco}\n")

print("\nExibindo os Dados dos Livros: ")
            