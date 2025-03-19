import os
os.system("clear")

contador = 0
continua = "s"

while continua == "s":
    #comando a serem repetidos
    print("Repetindo...")

    contador +=1

    continua = input("tecle 's' se deseja continuar.").strip().lower()

if contador == 0:
    print("O blobo NÃO foi repetido.")
else:
    print(f"bloco foi repetido (contador)vezes")