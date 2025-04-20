import os
os.system("cls || clear")

lista_numeros = []
quantidade_numero = (5)

for i in range(quantidade_numero):
    numero = int(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)

maior = max(lista_numeros)
menor = min(lista_numeros)
print()
for numero in lista_numeros:
    print(f"{i}º numero: {numero}")

print(f"\nmaior: {maior}")
print(f"\nmenor: {menor}")