import os

os.system("cls || clear")

print("Inicio do Programa!")



for i in range(4):
    nota = float(input(f"Digite o {i+1} número: "))
    soma += nota

media = soma / 4
print(f"media:", {media}) 


print("\nFim Do Programa!")