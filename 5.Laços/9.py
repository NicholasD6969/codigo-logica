import os 
os.system("cls || clear")

nota = int(input("Digite  a nota do aluno: "))

while True:
    if nota >10 or nota <0:
        print("notas de 0 a 10")
    else:
        break

print(f"nota {nota}")