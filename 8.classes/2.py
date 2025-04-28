import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class pessoa:
    nome: str
    idade: int
    peso: float
    altura: float

nome = str(input("Dgite seu nome: "))
idade = int(input("Dgite sua idade: "))
peso = float(input("Dgite seu peso: "))
altura = float(input("Dgite sua altura: "))

pessoa = pessoa (nome=nome, idade=idade, peso=peso, altura=altura )

print(f"Nome: {pessoa.nome} idade: {pessoa.idade} peso: {pessoa.peso} altura: {pessoa.altura}")