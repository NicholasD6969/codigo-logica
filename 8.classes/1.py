import os
os.system("cls || clear")
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str
    idade: int

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str
#atribuindo valores
pessoa1 = Pessoa("Alice", 30)    
pessoa2 = Pessoa("Bob", 25) 

pet1 = Pet("Toto", 4, "Pastor-alemão")
pet2 = Pet("Hulk", 6, "Pitbull")

print("\nDados de Pessoas: ")
print(f"Nome: {pessoa1.nome}, idade: {pessoa1.idade}")
print(f"Nome: {pessoa2.nome}, idade: {pessoa2.idade}")

print("\nDados dos Pets: ")
print(f"Nome: {pet1.nome}, idade: {pet1.idade}, raça: {pet1.raca}")
print(f"Nome: {pet2.nome}, idade: {pet1.idade}, raça: {pet1.raca}")