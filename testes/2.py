import os
from dataclasses import dataclass

os.system("cls || clear")

def verificar_carrinho(lista_roupas):
    if not lista_roupas:
        print("\nNão tem roupas nessa lista!")
        return True
    return False
    
def mostrando_estoque_roupa(estoque_roupas):
    if estoque_roupas:
        print("""
1 \t camisa basica R$ 120.00
2 \t camisa uv R$ 185.00
3 \t regata R$ 110.00
4 \t short R$ 155.00
5 \t chapéu R$ 90.00""")
    return

def adicionar_peca(lista_roupas):
        print("""
1 \t camisa basica R$ 120.00
2 \t camisa uv R$ 185.00
3 \t regata R$ 110.00
4 \t short R$ 155.00
5 \t chapéu R$ 90.00""")
        qual_roupa = int(input("Deseja qual roupa? "))
        if qual_roupa == 1:
            pecas = "camisa basica "
            valor = 120.00
        if qual_roupa == 2:
            pecas = "camisa uv "
            valor = 185.00
        if qual_roupa == 3:
            pecas = "regata " 
            valor = 110.00
        if qual_roupa == 4:
            pecas = "short "
            valor = 155.00
        if qual_roupa ==  5:
            pecas = "chapéu "
            valor = 90.00 
        
            return pecas, valor
      
           
roupas = []
while True:
    print("""
    -Gerenciador de Opções
    - Adicionar peças
    - Verificar Carrinho 
    - Verificar estoque
    - Remover
    - Sair""")
    opcao = int(input("Digite uma das opções acima: "))

    match opcao:
        case 1:
            ...(roupas)