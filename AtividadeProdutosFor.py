produtos = ["camiseta", "calça", "par meias", "boné", "touca"]
precos = [40.00, 80.00, 15.00, 20.00, 20.00]
quantidades = [2, 1, 2, 1, 1]
subtotais = []
# ANTES, FARIA ASSIM PARA PEGAR O PRODUTO E PREÇO:

print(f"O produto {produtos[0]} custa R${precos[0]}.")

for indice, produto in enumerate(produtos):
    preco = precos[indice] # preco = precos[0]
    quantidade = quantidades[indice]
    subtotal = quantidade * preco
    subtotais.append(subtotal)

    mensagem = f"""
    -----------------------------------
    Produto: {produto}
    Quantidade: {quantidade}
    Valor unitário: {preco}
    Subtotal: {subtotal}
    -----------------------------------
    """

    print(mensagem)

print(f"O total da compra deu: R${sum(subtotais)}")