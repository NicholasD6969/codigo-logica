import os
os.system("cls || clear")

def inflacionar(valor):
    return valor
print("PREÇO DE UM PRODUTO")
produto1 = float(input("digite o valor do produto: "))
if produto1 >=100:
    taxa = 1.20
else:
    taxa = 1.10
valor_final = produto1*taxa    
print(f"valor do juros é: {valor_final}")    

def descontar(valor):
    return valor
if produto1 >=100:
    taxa = 0.20
else:
    taxa = 0.10       
valor_final = produto1*taxa
print(f"valor do desconto é: {valor_final}")