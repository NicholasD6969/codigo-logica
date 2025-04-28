import os

os.system("cls || clear")

print("Inicio do Programa")
soma = 0
for i in range(5):
    nota = float(input(f"Digite o {i+1} número: "))
    soma = soma + nota

print(f"soam: {soma}")

print("FIM DO PROGRAMA!")