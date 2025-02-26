import os
os.system ("clear")

login = str(input("Login: "))
senha = str(input("Senha: "))

if  login or senha == False:
    print("Login e/ou Senha incorretos")
else:
    print("Seja Bem Vindo! ")

print(f"\nlogin: {Login}")