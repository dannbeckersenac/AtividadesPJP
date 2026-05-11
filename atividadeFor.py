# Salva na memória uma variável nome frutas, inserindo uma lista de frutas
frutas = ["manga", "banana", "abacaxi", "laranja", "uva"]

# Entrada do usuário pedindo para digitar nome da fruta favorita
fruta_favorita = input("Qual sua fruta favorita?: ")
# SE a fruta favorita NÃO ESTÁ NA lista frutas
if fruta_favorita not in frutas:
    # Faça isso (exibir mensagem e adiciona na lista):
    print("Sua fruta favorita não está na lista!")
    print("Adicionando...")
    frutas.append(fruta_favorita)


# PARA cada posição (índice) e fruta NA lista numerada de frutas
for posicao, fruta in enumerate(frutas):
    # Faça isso:
    # SE a fruta dessa iteração é igual a fruta favorita
    if fruta == fruta_favorita:
        # Salva numa nova variável a posição dessa iteração
        posicao_fruta_favorita = posicao
        # Quebra o for (faz ele parar)
        break 

# Saída do algoritmo (print)
print(f"Minha fruta favorita está na posição índice {posicao_fruta_favorita}")