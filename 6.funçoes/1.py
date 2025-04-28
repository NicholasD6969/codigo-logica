import os 


def logo_senai():
    os.system("cls || clear")
    print("==SENAI==")

logo_senai() #chamado a função
nome = input("Digite seu nome: ")

logo_senai()
idade = int(input("Digite a idade: "))

logo_senai()
print(f"Nome: {nome}")
print(f"Idade: {idade}")