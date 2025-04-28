import os
os.system("cls || clear")

def numero_negativo(numero):
    if numero <0 :
        print("esse numero é negativo")
    elif numero ==0:
        print("0 é neutro")
    else:
        print("esse numero é positivo")

print("Positivo E Negativo")
numero = int(input("Digite um numero: "))
numero_negativo(numero)
print("fim.")