import os
os.system("cls || clear")

Lista_Pratos = []
contador = 0

while True:
    opcoes = int(input("""
codigo \t prato \t\t\t valor
1 \t Picanha R$ 25.00
2 \t Bife acebolado R$ 15.00
3 \t Lasanha R$ 20.00
4 \t strogonoff R$ 15.00
5 \t pão com ovo R$ 5.00
Digite a opção desejada: """))
    match opcoes:
            case 1:
                prato = "Picanha"
                valor = 25,00
            case 2:
                prato = "Bife acebolado"
                valor = 15,00    
            case 3:
                prato = "Lasanha"
                valor = 20,00
            case 4:
                prato = "Strogonoff"
                valor = 15,00    
            case 1:
                prato = "Pão com ovo"
                valor = 5,00
            case _:
               break
              
    continuar = str(input("Deseja outro prato 'S' ou 'N': ")).upper() 
    if continuar == "N":
        break
    else:
        valor
        valor
        soma = valor + valor
        continue
print(f"prato: {prato}")
print(f"valor: {valor}")      
print(f"Valor final: {soma}")