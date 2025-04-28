import os
os.system("cls || clear")

print("\n Nota do aluno")
def saudação(nome_aluno):
    print(f"Nota de {nome_aluno}! ")
nome_aluno = input("Digite o nome do aluno: ")
saudação(nome_aluno)

lista_notas = []
quantidade_notas = 4
def calcular_media():
    for i in range(quantidade_notas):
        nota = float(input(f"Digite a {i+1} nota de {nome_aluno}: "))
        lista_notas.append(nota)

    media = sum(lista_notas) / 3
    return media
print()
def Aprovação():
    media_final = calcular_media()
    if media_final >= 7:
        print("Aprovado!")
    elif media_final >= 4:
        print("Recuperação!")
    else:
            print("Reprovado!")      
print(f"Media:", calcular_media())
