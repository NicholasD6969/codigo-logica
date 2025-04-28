import os
os.system("cls || clear")

lista_numeros = []
quantidade_numeros = (6)
quantidade_pares = ()
quantidade_impares = ()
for i in range(quantidade_numeros):
    numero = int(input(f"Digite o {i+1}º numero: "))
    lista_numeros.append(numero)

impar = (lista_numeros)
par = (lista_numeros)
print()
for numero in lista_numeros:
    print(f"{i}º numero: {numero}")

if numero %2 ==0:
    print("Par")
    quantidade_pares += 1
    
else:
    print("impar")    
    quantidade_impares += 1
print(f"\nimpar: {impar}")
print(f"\npar: {par}")
