import math

nota1 = float(input("Digite a nota 1: "))
nota2 = float(input("Digite a nota 2: "))
nota3 = float(input("Digite a nota 3: "))

media = (nota1 + nota2 + nota3) / 3
media = math.ceil(media)
# media = round(media, 1) 
print("A média foi de:", media)

# Se a media é maior que sete então está aprovado
if media >= 7:
    print("Aprovado!")

elif media < 7 and media >=5:
    print("Em recuperação!")

else:
    print("Reprovado!")