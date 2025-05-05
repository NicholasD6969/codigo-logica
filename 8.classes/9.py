import os
from dataclasses import dataclass
os.system("cls || clear")

lista_livros = {}
@dataclass
class Autor:
    nome: str
    bibliografia: str

class Livro:
    titulo: str
    ano: int

    def exibir_detalhes(self):
        print(f"\nNome: {self.nome} \nTitulo: {self.titulo} \nAno: {self.ano}")
livro = Livro(
    titulo = input("Digite o titulo do livro: "),
    ano = int(input("Digite o da publicação: ")),
    autor = Autor(
        nome = input("Digite o nome do Autor: "),
        bibliografia = input("Digite as informações de bibliografia do autor: ")
    )
        )
lista_livros.append(livro)

print(f"\n Salvando dados: ")
nome_arquivo = "dados_livro.txt"
with open(nome_arquivo, "a", encoding="utf-8") as arquivos_livros:
    for livro in lista_livros:
        arquivos_livros.write(f"{livro.ano}, {livro.autor.nome}") 