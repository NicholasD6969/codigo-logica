import os
os.system ("clear")

idade = 20

#se idade <18 entao
#   esreval("acesso negado.")
# senao
#   escreval ("acesso permitido.")
#fimse

if idade < 12:
    print("acesso negado. ")
elif idade < 18:
    print("somente com permissao dos pais")    
else:
    print("acesso permitido. ")

    print("== Fim ==")

