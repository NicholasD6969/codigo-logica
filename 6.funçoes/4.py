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

print(f"somar: {soma}")
print(f"subtrair: {subtracao}")
print(f"multiplicar: {multiplicacao}")
print(f"divisão: {divisao}")




#faça uma função sem retorno com o nome: logo_senai()
#Limpando o terminal e inserindo: == SENAI DENDEZEIROS ===

#solicite ao usuario 2 numeros
#cada um em uma variavel diferente
#Crie uma funçao com retorno para somar os 2 numeros informados pelo usuario