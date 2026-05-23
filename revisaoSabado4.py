nomes = ["Daniel", "João", "Pedro", "Luana", "Luciana"]
notas = [8, 9, 3, 5, 10]
frequencias = [90, 65, 75, 55, 100]

for posicao_nome, nome in enumerate(nomes):
    
    nota = notas[posicao_nome]
    frequencia = frequencias[posicao_nome]

    if nota >= 7 and frequencia >= 75:
        print(f"{nome} Passou!")

    else:
        print(f"{nome} Reprovou!")