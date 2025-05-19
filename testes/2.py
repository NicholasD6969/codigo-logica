import os
from dataclasses import dataclass

# Limpa o terminal
os.system("cls" if os.name == "nt" else "clear")

print("\nZIP NAUTICA")

@dataclass
class Roupas:
    escolha: str

    def exibir_dados(self):
        print(f"Roupas: {self.escolha}")

# Catálogo da loja
catalogo = {
    "Camisa Basica": 120.00,
    "Camisa Uv": 185.00,
    "Bermuda": 155.00,
    "Regata": 105.00,
    "Chapéu": 90.00
}

def menu():
    carrinho = []

    def mostrar_catalogo():
        print("\n-- Catálogo da Zip Nautica --")
        for i, (nome, preco) in enumerate(catalogo.items(), 1):
            print(f"{i}. {nome} - R${preco:.2f}")

    def adicionar_roupas():
        mostrar_catalogo()
        escolha = input("Digite o nome da peça que deseja adicionar: ")
        if escolha in catalogo:
            roupa = Roupas(escolha)
            carrinho.append(roupa)
            print(f"{escolha} adicionada ao carrinho!")
        else:
            print("Roupa não encontrada no catálogo.")

    def exibir_roupas():
        if carrinho:
            print("\n-- Seu Carrinho --")
            total = 0
            for roupa in carrinho:
                roupa.exibir_dados()
                total += catalogo.get(roupa.escolha, 0)
            print(f"Total: R${total:.2f}")
        else:
            print("Nenhuma roupa no carrinho.")

    def trocar_peca():
        if not carrinho:
            print("Seu carrinho está vazio.")
            return
        print("\n-- Carrinho Atual --")
        for i, item in enumerate(carrinho, 1):
            print(f"{i}. {item.escolha}")
        try:
            indice = int(input("Digite o número da peça que deseja trocar: ")) - 1
            if 0 <= indice < len(carrinho):
                mostrar_catalogo()
                nova = input("Digite o nome da nova roupa: ")
                if nova in catalogo:
                    carrinho[indice] = Roupas(nova)
                    print(f"Peça trocada por {nova}.")
                else:
                    print("Nova roupa não encontrada no catálogo.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    def remover_roupa():
        if not carrinho:
            print("Não tem roupas no carrinho.")
            return
        print("\n-- Carrinho Atual --")
        for i, item in enumerate(carrinho, 1):
            print(f"{i}. {item.escolha}")
        try:
            indice = int(input("Digite o número da roupa que deseja remover: ")) - 1
            if 0 <= indice < len(carrinho):
                removida = carrinho.pop(indice)
                print(f"{removida.escolha} removida do carrinho.")
            else:
                print("Número inválido.")
        except ValueError:
            print("Entrada inválida.")

    # Loop do menu principal
    while True:
        print("\n--- Menu Da Zip Nautica ---")
        print("1. Adicionar roupa")
        print("2. Trocar peça")
        print("3. Exibir carrinho e total")
        print("4. Remover roupa")
        print("5. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_roupas()
        elif escolha == "2":
            trocar_peca()
        elif escolha == "3":
            exibir_roupas()
        elif escolha == "4":
            remover_roupa()
        elif escolha == "5":
            print("Obrigado por visitar a loja!")
            break
        else:
            print("Opção inválida. Tente novamente.")
os.system("cls || clear")
# Inicia o programa
menu()
