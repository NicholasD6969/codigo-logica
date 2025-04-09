import os
os.system("cls || clear")

def numero_par(numero):
    if numero % 2 == 0:
        print("esse numero é par")
    else:
        print("esse numero é impar")

print("PARES E IMPARES")
numero = int(input("Digite um numero: "))
numero_par(numero)
print("fim.")            