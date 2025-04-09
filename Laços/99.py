import os
os.system("cls || clear")

contador = 0
opcao = 0
soma = 0
pagamento = 0
while True:
    opcao = int(input("""
código \t Prato \t\t\t valor
1 \t Picanha \t\t R$ 25,00
3 \t strogonoff \t R$ 18,00
4 \t Bife acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00
6 \t Refrigerante \t R$ 6,00                  
7 \t Suco \t R$ 2,00
Digite a opção desejada:
"""))

    match opcao:
        case 1:
            prato = "Picanha"
            valor = 20,00
        case 2:
            prato = "Lasanha"  
            valor = 25,00
        case 3:
            prato = "strogonoff"
            valor =  18,00
        case 4:
            prato = "Bife acebolado"
            valor =  15,00
        case 5:
            prato = "Pão com ovo"
            valor =  5,00
        case 6:
            prato = "refrigerante"
            valor =  6,00
        case 7:
            prato = "suco"
            valor = 2,00    
        case _:
            "prato invalido"

    outro_pedido = str(input("Deseja outro patro? ")).upper()
    if outro_pedido == 'S':
        valor += valor
        continue
    else:   
        break

    pagamento = input("Qual a forma de pagamento? \n 'À vista' ou 'Cartão de credito' ")    
    if pagamento == "À vista":
        valor *= 0.10
        break
    else:
        valor *= 1.10 
        break

print(f"pagamento: {pagamento}")
print(f"opcao: {opcao}")
print(f"valor: {valor}")
