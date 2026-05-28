while True:
    menu = """
    ================================
    Calculadora:
    1 - Soma (+)
    2 - Subtração (-)
    3 - Multiplicação (x)
    4 - Divisão (/)
    0 - Sair
    ================================
    """
    print(menu)
    opcao = input("Escolha uma opção acima e digite: ")

    if opcao == "0": 
        
        break

    if opcao not in ["1", "2", "3", "4", "0"]:
        print("Opção inválida! Tente novamente!")
        continue

    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    if opcao == "1":
        total = n1 + n2
        print(f"{n1} + {n2} = {total}")
    elif opcao == "2":
        total = n1 - n2
        print(f"{n1} - {n2} = {total}")
    elif opcao == "3":
        total = n1 * n2
        print(f"{n1} x {n2} = {total}")
    elif opcao == "4":
        if n2 == 0: print("Não é possível dividir por zero!")
        else: print(f"{n1} / {n2} = {round(n1 / n2, 2)}")
     
    else:
        print("Opção Inválida!")   