import os
os.system("clear")

primeiro_numero = float(input("Digite o numero"))
segundo_numero = float(input("Digite o numero"))

if  primeiro_numero > segundo_numero:
    maior = primeiro_numero
    menor = segundo_numero
else:
    maior = primeiro_numero
    menor = segundo_numero

print(f"\nmaior: {maior}")
print(f"\nmenor: {menor}")