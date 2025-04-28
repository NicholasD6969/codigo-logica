import os
os.system("cls \\ clear")

contador = 0 
soma = 0

while True:
    nota = float(input("Digite a nota: "))
    reposta = input("Digite inserir mais uma nota? \nDigite 's' ou 'N'").upper()
    if reposta == "N":
        break
    else:
        contador += 1
        soma += nota

    if contador == 0:
        soma = nota
        contador = 1

        media = soma / contador

    print(f"\nMédia: {media}")