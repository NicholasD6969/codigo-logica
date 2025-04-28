import os
os.system("clear")

aluno = input("digite seu nome: ")
nota_1 = float(input("digite a primeira nota: "))
nota_2 = float(input("Digite a segunda nota: "))

media = (nota_1 + nota_2)/2

if media >= 9:
    conceito = ("A")
elif media >= 7.5:
    conceito = ("B")
elif media >= 6:
    conceito = ("C")    
elif media >= 4:
    conceito = ("D")    
else:
    conceito = ("E") 

match conceito:
    case "A" | "B" | "C":
        print(f"conceito: {conceito}")
        print(("aprovado."))
    case "D"| "E":
        print(f"Conceito: {conceito}") 
        print("Reprovado.")
    case _:
        print("Opção invalída.") 
