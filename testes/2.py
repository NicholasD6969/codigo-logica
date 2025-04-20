print("Cardápio:")
print("1 - Hambúrguer - R$15.00")
print("2 - Pizza - R$25.00")
print("3 - Salada - R$12.00")
print("4 - Refrigerante - R$6.00")
print("5 - Suco Natural - R$8.00")
print("6 - Batata Frita - R$10.00")
print("7 - Sorvete - R$7.00")

total = 0
pedido1 = ""
pedido2 = ""
pedido3 = ""
pedido4 = ""
pedido5 = ""

codigos = ""
nomes = ""

contador = 0

while True:
    codigo = int(input("Digite o código do prato desejado (ou 0 para encerrar): "))

    if codigo == 0:
        break

    if codigo == 1:
        total += 15.0
        codigos += "1 "
        nomes += "Hambúrguer, "
    elif codigo == 2:
        total += 25.0
        codigos += "2 "
        nomes += "Pizza, "
    elif codigo == 3:
        total += 12.0
        codigos += "3 "
        nomes += "Salada, "
    elif codigo == 4:
        total += 6.0
        codigos += "4 "
        nomes += "Refrigerante, "
    elif codigo == 5:
        total += 8.0
        codigos += "5 "
        nomes += "Suco Natural, "
    elif codigo == 6:
        total += 10.0
        codigos += "6 "
        nomes += "Batata Frita, "
    elif codigo == 7:
        total += 7.0
        codigos += "7 "
        nomes += "Sorvete, "
    else:
        print("Código inválido. Tente novamente.")

print("\nFormas de pagamento:")
print("1 - À vista (10% de desconto)")
print("2 - Cartão de crédito (10% de acréscimo)")

pagamento = int(input("Escolha a forma de pagamento (1 ou 2): "))

if pagamento == 1:
    desconto = total * 0.10
    total_final = total - desconto
    forma = "À vista"
elif pagamento == 2:
    desconto = total * 0.10
    total_final = total + desconto
    forma = "Cartão de crédito"
else:
    print("Forma de pagamento inválida. Considerando valor total sem alteração.")
    total_final = total
    forma = "Não informada"

print("\nResumo do pedido:")
print("Códigos dos pratos:", codigos)
print("Nomes dos pratos:", nomes)
print("Subtotal: R$%.2f" % total)
print("Forma de pagamento:", forma)
print("Valor final: R$%.2f" % total_final)