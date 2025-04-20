import os
os.system("cls || clear")

print("==ZIP NAUTICA==")
contador = 0

def escolha(opcoes):
    return opcoes
while True:
    opcoes = int(input("""
codigo \t peça \t\t\t valor
1 \t camisa basica R$ 120.00
2 \t camisa uv R$ 185.00
3 \t regata R$ 110.00
4 \t short R$ 155.00
5 \t chapéu R$ 90.00
Digite a opção desejada: """))
    match opcoes:
        case 1:
            pecas = "camisa basica "
            valor = 120.00
        case 2:
            pecas = "camisa uv "
            valor = 185.00
        case 3:
            pecas = "regata " 
            valor = 110.00
        case 4:
            pecas = "short "
            valor = 155.00
        case 5:
            pecas = "chapéu "
            valor = 90.00 
        case _:
            break   
    print("peça:", pecas) 
    print("valor:", valor)    

    continuar = str(input("Deseja outra peça de roupa 'S' ou 'N': ")).upper() 
    if continuar == "N":
        break
    else:
        valor
        valor
        soma = valor + valor
        continue

print("\nFormas de pagamento: ")
print("1- À vista (10% de desconto)")   
print("2- Cartão de credito (10% de acréscimo)") 
forma_pagamento = int(input("Qual a forma de pagamento '1- À vista' ou '2- Cartão de credito': "))
if forma_pagamento == 1:
    soma * 0.10
    forma = "À vista"
elif forma_pagamento == 2:
    soma * 1.10
    forma = "Cartão de credito"
else:
    print("Forma de pagamento invalida")


print("valor:", valor) 
print("forma de pagamento:", forma)   
print("valor final:", soma)   