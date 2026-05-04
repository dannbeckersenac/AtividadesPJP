nota = float(input("Digite a nota do aluno: "))

if nota >= 0 and nota <= 5.5:
    print("Não atendido")

elif nota > 5.5 and nota <= 6.5:
    print("Regular")

elif nota > 6.5 and nota <= 10:
    print("Atendido")

else:
    print("Número não condiz com uma nota de 0 a 10")

    