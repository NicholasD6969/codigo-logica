import os
os.system("cls || clear")

soma = 0
        
def calcular(media):
    return soma/2

for i in range(2):
    nota = float(input("Digite uma nota: "))
    soma += nota   

media = calcular(soma)

if nota >=7:
    print("aprovado")
else:
    print("Reprovado")    
print(f"Media: {media}")