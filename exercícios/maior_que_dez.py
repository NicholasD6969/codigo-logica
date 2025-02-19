    #LLimpar o terminal.
import os
os.system("clear")

#Elabore um alogoritimo para solicitar ao usuário um valor e
#escrever a mensagem: É MAIOR QUE 10!
#se o valor lido forb maior que 10, caso contrário escrever:
#Não é maior que 10!

numero =  int(input("digite o numero: "))
 
if numero == 10:
    print ("É igual a 10. ")
elif numero > 10: 
    print("é maior que 10")
else: print ("nao é maior que 10")

print("==FIM==")
    


    
    
