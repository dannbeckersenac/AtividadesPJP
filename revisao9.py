produtos = ["arroz" ,"feijão", "ovos"]
precos = [4.99 ,6.99, 12.99]

for posicao_produto, produto in enumerate(produtos):
    
    if precos[posicao_produto] < 10:
        preco_ajustado = round(precos[posicao_produto] * 1.10, 2)
        print(f"Produto: {produto} custava R${precos[posicao_produto]} \
              e subiu para R${preco_ajustado}")
    else:
        print(f"Produto: {produto} custa R${precos[posicao_produto]}")