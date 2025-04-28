import os
os.system("cls || clear")

def calcular_media(primeira_nota, segunda_nota):
    soma = primeira_nota + segunda_nota
    media = soma/2
    return media

primeiro_numero = int(input("Digite o primeiro: "))
segundo_numero = int(input("Digite o segundo: "))

media = calcular_media(primeiro_numero, segundo_numero)
if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")  

print(f"Média: {media}")