import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_numeros = []
quantidade_positivos = 0
for i in (QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)

for numero in lista_numeros:
    print(f"{i}º numero: {numero}")
    if numero <0:
        numero * 0
    else:
        quantidade_positivos 

print(f"quantidade_positivos: {quantidade_positivos}")
     