import os
os.system("clear")

numero_1 = int(input("Digite quantas participação o Bahia tem na Libdertadores: "))
numero_2 = int(input("Digite quantas participação o Vitória tem na Libdertadores: "))

participacao = 

if participacao >0:
    participacao = "orgulho do Nordeste."
elif participacao <=0:
    participacao = "minusculo do Nordeste."
else:
    participacao = "invalído"

match participacao:
    case "orgulho do Nordeste.":
        print(f"Participacao na Libertadores: {participacao}")
        print(("É o ixquadrao. "))
    case "minusculo do Nordeste.":
        print(f"Participacao na Libertadores: {participacao}")
        print(("Galinhas. "))
    case _:
        print("Opção invalída.")    