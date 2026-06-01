import math

def calcular_media(notas: list) -> float:
    media = sum(notas) / len(notas)
    return math.ceil(media)

contador = 1
notas = []

while True:
    nota = float(input(f"Digite a nota {contador} ou -1 para sair: "))
    
    if nota == -1:
        break

    notas.append(nota)
    print("Nota foi registrada!")

print(notas)
media = calcular_media(notas)
print("A média foi de:", media)

# Se a media é maior que sete então está aprovado
if media >= 7:
    print("Aprovado!")

elif media < 7 and media >=5:
    print("Em recuperação!")

else:
    print("Reprovado!")