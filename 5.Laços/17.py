import os
os.system("cls || clear")

contador = 0
soma_salario = 0
maior_idade = 0
menor_idade = 9999
quantidade = 0

while True:
    opcao =  print("""
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
            contador += 1
            soma_salario += salário
            maior_idade = max(maior_idade, idade)
            menor_idade = min(menor_idade, idade)
            if sexo == "f" and salário >= 5000:
                mulheres5k += 1
        case 2:
                if contador > 0:
                    print(f"a idade é {idade}")
                    print(f"o sexo é {sexo}")
                    print(f"o salario é {salário}")
        case 3:
            print("Fim.")
            break
        case _:
            ("Opção invalida!")

            if idade >= 18:
                print("Maior de idade")        
            else:
                print("menor de idade")
            