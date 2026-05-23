velocidade = int(input("Digite aa velocidade: "))

if velocidade > 0 and velocidade <= 60:
    print("Está andando e dentro do limite")
elif velocidade > 60 and velocidade <= 80:
    print("Está acima da velocidade!")
elif velocidade > 80:
    print("Está muito acima, multa!")
elif velocidade == 0:
    print("Veículo está parado!")
else:
    print("Número digitado inválido!")