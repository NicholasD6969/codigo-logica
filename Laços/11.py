import os
os.system("cls || clear")

login_ = "Nicholas"
senha_ = "1502"
QUANTIDADE_DE_TENTATIVAS = (3)

for i in range (QUANTIDADE_DE_TENTATIVAS):

    login = input("Digite o Login:")
    senha = input("Digite sua senha: ")
    if login_ == login and senha_ == senha:
        print("Usuario e senha corretos!")
        break
    else:
            print("login ou senha invalídos.")
    if i == 2:
            print("voçê chegou ao seu limite")

               