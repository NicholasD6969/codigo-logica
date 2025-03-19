import os
import time
os.system("cls || clear")

print("INICIO DO PROGRAMA!")

numero = int(input("Digite um Numero: "))

for i in range(9,0,-1):
    print(f"{numero} x {i} = {numero * 1}")
    time.sleep(0.0)

print("FIM DO PROGRAMA!")    