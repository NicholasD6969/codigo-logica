import os
os.system ("clear")

login = str(input("Login: "))
senha = str(input("Senha: "))

if  login or senha == False:
    print("Login e/ou Senha incorretos")
else:
    print(f"\nlogin: {login}")

print("seja bem vindo")
