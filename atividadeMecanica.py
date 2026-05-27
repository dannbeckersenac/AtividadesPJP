# Listas de Produtos
produtos = ["Pneu Aro 15", "Bateria 60Ah", "Óleo de Motor", "Palheta do Limpador"]
precos_produtos = [450.00, 350.00, 60.00, 40.00]
# Listas de Serviços
servicos = ["Troca de Óleo", "Alinhamento", "Revisão Completa", "Lavagem Simples"]
precos_servicos = [50.00, 150.00, 600.00, 80.00]

print("Bem-vindo à Auto Peças!")
escolha_tipo = input("Você deseja produtos ou serviços? ")

# Verifica a escolha
if escolha_tipo == "Produto":
    print("\n--- CATÁLOGO DE PRODUTOS ---")
    for i, item in enumerate(produtos):
        print(f"[Código {i}] {item} - R$ {precos_produtos[i]}")

elif escolha_tipo == "Serviço":
    print("\n--- CATÁLOGO DE PRODUTOS ---")
    for i, item in enumerate(servicos):
        print(f"[Código {i}] {item} - R$ {precos_servicos[i]}")

else:
    print("Escolha inválida!")
    exit()

codigo = int(input("Digite o código do que você quer: "))

if escolha_tipo == "Produto":
    nome_escolhido = produtos[codigo]
    preco_escolhido = precos_produtos[codigo]

elif escolha_tipo == "Serviço":
    nome_escolhido = servicos[codigo]
    preco_escolhido = precos_servicos[codigo]

if preco_escolhido >= 300:
    preco_escolhido = round(preco_escolhido * 0.90, 2)

mensagem = f"""
===================================
Item: {nome_escolhido}
Preço: {preco_escolhido}
===================================
"""

print(mensagem)