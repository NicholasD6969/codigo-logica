import os

os.system("cls || clear")

def tabuada(numero):
    for i in range(1,11):
        print(f"{numero} * {i} = {numero * i}")

print("== TABUADA ==")
numero = int(input("Digite um número: "))
tabuada(numero)        