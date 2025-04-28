import os 
os.system("cls || clear")

print("Notas e média")

soma = 0
for i in range (4):
    nota = float(input(f"digite a {i + 1} nota: "))
    soma = + nota
    média = soma/4
print(f"média: {média}")    