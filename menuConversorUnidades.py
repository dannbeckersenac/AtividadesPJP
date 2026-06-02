def exibir_menu():
    print("\n===================")
    print("Menu:")
    print("1 - Converter celsius para Fahrenheit.")
    print("2 - Converter reais para dólares.")
    print("3 - Converter horas para minutos).")
    print("0 - Sair.")
    print("===================")

def converter_celsius():
    celsius = float(input("Digite quantos graus celsius: "))
    fh = celsius * 1.8 + 32
    print(f"Fahreinheit = {round(fh, 2)}")

def converter_reais():
    reais = float(input("Digite o valor em R$ que deseja converter: "))
    dolares = reais / 5
    print(f"O total deu U${round(dolares, 2)}")

def converter_horas():
    horas = float(input("Digite a quantidade de horas para converter: "))
    minutos = horas * 60
    print(f"São {minutos} minutos.")


while True:
    exibir_menu()
    opcao = input("Escolha a opção: ")

    if opcao == "0":
        break
    elif opcao == "1":
        converter_celsius()
    elif opcao == "2":
        converter_reais()
    elif opcao == "3":
        converter_horas()
    else:
        print("Opção inválida!")