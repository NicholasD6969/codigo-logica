import os
os.system("clear")

#Math-case substituit o uso do if-elif-else

dia = input("Digite dia da semana: ")

match dia:
    case "segunda":
        print("Hoje é segunda-feira")
    case "terça":
        print("Hoje é terça-feira")
    case "quarta":
        print("Hoje é quarta-feira")
    case "quinta":
        print("Hoje é quinta")
    case "sexta":
        print("Hoje é sexta-feira")
    case "sábado" | "domingo":
        print("Hoje é fim de semana")
    case _:
        print("Dia invalido.")

        print(dia) 
        print("==Fim==")                