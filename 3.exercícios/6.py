import os
os.system("clear")

idade = int(input("Digite sua idade: "))


if idade >= 18 and idade <= 65:
 resultado = ("Voto obrigatótio.")

else:
 resultado = "Não é obrigado a votar. "

print(f"\nresultado: {resultado}")