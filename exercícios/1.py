import os
os.system("clear") 

primeira_nota = float(input("Digite sua primeira nota: "))
segunda_nota = float(input("Digite sua segunda nota"))
terceira_nota = float(input("Digiteb sua terceira nota"))

soma = primeira_nota + segunda_nota + terceira_nota
media = soma/3


print(f"media: (media)")

if media > 7:
    print("aprovado")
else:
    print("reprovado")
