import os
os.system


opçao = int(input("""
código \t Prato \t\t\t valor
1 \t Picanha \t\t R$ 25,00
3 \t strogonoff \t R$ 18,00
4 \t Bufe acebolado \t R$ 15,00
5 \t Pão com ovo \t\t R$ 5,00

Digite a opção desejada:
"""))

match opçao:
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
        prato = "Bufe acebolado"
        valor =  15,00
    case 5:
        prato = "Pão com ovo"
        valor =  5,00
        print(f"\prato escolhido: {prato}")                 
        print(f"\valor: {valor}") 

        print("==FIM==")              
        
