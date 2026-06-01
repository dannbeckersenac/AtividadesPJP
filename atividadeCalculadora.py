
def somar(n1, n2):
    total = n1 + n2
    print(f"{n1} + {n2} = {total}")

def subtrair(n1, n2):
    total = n1 - n2
    print(f"{n1} - {n2} = {total}")

def multiplicar(n1, n2):
    total = n1 * n2
    print(f"{n1} x {n2} = {total}")

def dividir(n1, n2):
    if n2 == 0: print("Não é possível dividir por zero!")
    else: print(f"{n1} / {n2} = {round(n1 / n2, 2)}")

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

    if opcao == "1": somar(n1, n2) 
    elif opcao == "2": subtrair(n1, n2)    
    elif opcao == "3": multiplicar(n1, n2)   
    elif opcao == "4": dividir(n1, n2)

     
    else:
        print("Opção Inválida!")   




print("Somando fora do while...")
somar(5, 5)
