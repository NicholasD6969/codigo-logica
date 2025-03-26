import os
os.system("cls || clear")

while True:
    print("""
CÓDIGO | DESCRIÇÃO
1      | ADCIONAR PESSOAS
2      | EXIBIR RESULTADOS
3      | SAIR
""")

    opção = int(input())

    match opção:
        case 1:
            idade = int(input("digite sua idade: "))
            sexo = input("digite seu sexo: \n digite 'f' ou 'm': ").upper()
            salário = input("informe o salário: ")
        case 2:
            print(f"a idade é {idade}")
            print(f"o sexo é {sexo}")
            print(f"o salario é {salário}")
        case 3:
            print("Fim.")
        case _:
            ("Opção invalida!")

        if idade >= 18:
            print("Maior de idade")        
        else:
            print("menor de idade")