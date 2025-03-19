import os
os.system("cls || clear")

login_ = "Nicholas"
senha_ = "1502"

while True:
    login = input("Digite o Login:")
    senha = input("Digite sua senha: ")
    if login_ == login and senha_ == senha:
        print("Usuario e senha corretos!")
        break
    else:
        print("login ou senha invalídos")
           

print(f"login {login}")    
print(f"senha {senha}")    