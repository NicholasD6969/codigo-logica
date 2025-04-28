import os

def log_senai():
    os.system("cls || clear")
    print("==SENAI DENDEZEIROS==")

def somar(numero1, numero2):
    return numero1 + numero2

def subtrair(numero1, numero2):
    return numero1 - numero2

def multiplicar(numero1, numero2):
    return numero1 * numero2

def dividir(numero1, numero2):
    return numero1 / numero2

log_senai()
numero1 = int(input("Digite um numero: "))
log_senai()
numero2 = int(input("Digite outro numero: "))

soma = somar(numero1, numero2)
subtracao = subtrair(numero1, numero2)
multiplicacao = multiplicar(numero1, numero2)
divisao = dividir(numero1, numero2)

print(f"soma: {soma}")
print(f"subtração: {subtracao}")
print(f"multiplicação: {multiplicacao}")
print(f"divisão: {divisao}")