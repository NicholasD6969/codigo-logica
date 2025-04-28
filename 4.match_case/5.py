import os 
os.system("clear")

valor_produto = int(input("Digitr valor do produto"))
forma_pagamento = int(input("""
1 = A vista
2 = A prazo
Digite a for de pagamento"""))                           

match forma_pagamento:
    case 1:
        #aplicamento desconto de 10%
        desconto = valo_produto * 0,10
        valor_pagar = valor_produto - desconto

        print(f"\nValor do produto: R$ {valor_produto}")
        print(f"Forma de pagamento: à vista")
        print(f"Valor do desconto: R$ {desconto}")
    case 2:

          
    case _:
        print("opção invalída")

    
    