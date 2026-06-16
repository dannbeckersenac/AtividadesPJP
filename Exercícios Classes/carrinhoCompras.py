class Produto:
    def __init__(self, nome, preco, setor):
        self.nome = nome
        self.preco = preco
        self.setor = setor

    def exibir(self):
        print(f"Nome: {self.nome} | Preço: {self.preco} | Setor: {self.setor}")
    
def exibir_menu():
    print("\n====================")
    print("1 - Cadastrar Produto")
    print("2 - Calcular Total")
    print("3 - Filtrar por Setor") 
    print("0 - Sair")
    print("====================")

# Opção 1
def cadastrar_produto():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto: "))
    setor = input("Digite o setor do produto: ")
    produto = Produto(nome, preco, setor)
    carrinho.append(produto)

# Opção 2
def exibir_produtos_e_total():
    if not carrinho:
        print("Não há produtos cadastrados!")
        print("Total do carrinho: R$0.0")
        return
    
    total = 0
    for produto in carrinho:
        produto.exibir()
        total += produto.preco
    print(f"Total do carrinho: R${total}")
    
def filtrar_por_setor():
    setor = input("Setor para filtrar: ")
    encontrou = False
    for codigo_produto, produto in enumerate(carrinho, start=1):
        if setor == produto.setor:
            print(f"Código produto: {codigo_produto}")
            produto.exibir()
            encontrou = True
    
    if not encontrou:
        print(f"Nenhum produto do setor digitado ({setor}) foi encontrado no carrinho.")
    

carrinho = []
while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar_produto()
    elif opcao == "2":
        exibir_produtos_e_total()
    elif opcao == "3":
        filtrar_por_setor()
    else:
        print("Opção Inválida")