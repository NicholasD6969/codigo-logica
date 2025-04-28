import os
os.system("cls || clear")

QUANTIDADE_NUMEROS = 5
lista_numero = []
quantidade_negativos = 0
soma_positivos = 0

for i in range(QUANTIDADE_NUMEROS):
    numero = int(input(f"Digite o {i+1}º  numero: "))
    lista_numero.append(numero)

for numero in lista_numero:
    if numero <0:
        quantidade_negativos += 1
    else:
        soma_positivos += numero
print(f"positivo: {soma_positivos}")    
print(f"negativo: {quantidade_negativos}")    