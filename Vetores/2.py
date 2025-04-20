import os
os.system("cls || clear")

lista_notas = []
quantidade_notas = 4

for i in range(quantidade_notas):
    nota = float(input("Digite uma nota: "))
    lista_notas.append(nota)
media = sum(lista_notas) / quantidade_notas
   
print()
for nota in lista_notas:
    Resultado = (nota)  
if media >=7:
    Resultado = ("aprovado")
elif media >=5:
    Resultado = ("recuperação")
else:
    Resultado = ("reprovado")     
print(f"Média: {media}")  
print(f"resultado: {Resultado}") 