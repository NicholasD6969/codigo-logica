import os
os.system("cls || clear")

peso = float(input("Digite o seu peso: "))
altura = float(input("Digite a sua altura: "))

def calcular_imc (peso, altura):
    imc = peso / altura **2
    return imc

if calcular_imc(peso, altura) <= 19.0:
    print("Abaixo do peso")
elif calcular_imc(peso, altura) <= 25.0:
    print("peso normal")
elif calcular_imc(peso, altura) <= 30.0:
    print("Sobrepeso")
elif calcular_imc(peso, altura) <= 35.0:
    print("Obesidade Grau 1")
elif calcular_imc(peso, altura) <= 40.0:
    print("Obesidade  Grau 2")
else:
    print("Obesidade Grau 3")

print(f"O seu IMC é: {calcular_imc(peso, altura)}")       