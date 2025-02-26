import os 
os.system("clear")

valor_produto = int(input("Digitr valor do produto"))
forma_pagamento = int(input("""
1 = A vista
2 = A prazo
Digite a for de pagamento""")                            

match forma_pagamento:
    case 1:
        #aplicamento desconto de 10%
        desconto = valo_produto * 0,10
    case 2:
          
    case _:
    print("Opçao inválida")

       
       
       print("==FIM==")       