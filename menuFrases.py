def exibir_menu():
    print("\n===================")
    print("Menu:")
    print("1 - Boas-vindas!")
    print("2 - Sobre o curso.")
    print("3 - Ajuda (sobre o exercício).")
    print("0 - Sair.")
    print("===================")

# Opção 1 (ELIF)
def saudacao():
    nome = input("Digite seu nome: ")
    print(f"Bem-vindo ao curso, {nome}!")

# Opção 2 (ELIF)
def sobre():
    print("O curso Jovem Programador, nesse primeiro semestre, tem o intuito de aprender conceitos básicos de algoritmos com Python e banco de dados Mysql.")

# Opção 3 (ELIF)
def ajuda():
    print("O programa cria um menu infinito usando While, com o objetivo de exibir mensagens na tela.")


while True:
    exibir_menu()
    opcao = input("Escolha a opção: ")

    if opcao == "0": break
    elif opcao == "1": saudacao()
    elif opcao == "2": sobre()
    elif opcao == "3": ajuda()
    else: print("Opção inválida!")
