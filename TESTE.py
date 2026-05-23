nomes = ["Daniel", "João", "Pedro", "Luana", "Luciana"]
notas = [8, 9, 3, 5, 10]
frequencias = [90, 65, 75, 55, 100]

for posicao_nome, nome in enumerate(nomes):
    
    nota = notas[posicao_nome]
    frequencia = frequencias[posicao_nome]
    
    motivo_nota = False
    motivo_frequencia = False

    if nota < 7:
        motivo_nota = True
    
    if frequencia < 75:
        motivo_frequencia = True
    
    if motivo_nota is True and motivo_frequencia is True:
        print(f"{nome} reprovado por nota e frequencia!")
    elif motivo_nota is True and motivo_frequencia is False:
        print(f"{nome} Reprovado por nota!")
    elif motivo_nota is False and motivo_frequencia is True:
        print(f"{nome} Reprovado por frequencia!")
    else:
        print(f"{nome} Aprovado!")

