class Aluno:
    def __init__(self, nome: str, notas: list):
        self.nome = nome
        self.notas = notas
    
    def exibir(self):
        print(f"Nome: {self.nome}")
        if not self.notas:
            print("Não possui notas lançadas.")
            return
        
        for ordem_nota, nota in enumerate(self.notas, start=1):
            print(f"Nota nº {ordem_nota}: {nota}")

    def situacao(self):
        ...
        # Aqui vocês vão fazer a lógica de somar:
        self.notas
        if not self.notas:
            print("Não foi possível ver a média pois não há notas lançadas.")
            return
        # ... e fazer o cálculo da média.
        media = sum(self.notas)  / len(self.notas)
        # por fim, dizer se está aprovado ou reprovado
        if media >= 6:
            print(f"Média: {media}. Aluno aprovado!")
        else:
            print(f"Média: {media}. Aluno reprovado!")

def exibir_menu():
    print("\n====================")
    print("1 - Cadastrar aluno")
    print("2 - Lançar notas")
    print("3 - Ver situação") 
    print("4 - Listar alunos")
    print("0 - Sair")
    print("====================")

# Opção 1
def cadastrar_aluno():
    nome = input("Digite o nome do aluno: ")
    aluno = Aluno(nome, [])
    alunos.append(aluno)
    print(f"Aluno {nome} cadastrado com sucesso!")

# Opção 2
def lancar_nota():
    codigo_aluno = int(input("Digite o código do aluno: ")) - 1
    aluno = alunos[codigo_aluno] # Aluno("Daniel", [])
    nota = float(input("Digite a nota para ser lançado: "))
    aluno.notas.append(nota)
    print(f"Nota {nota} lançada para o aluno {aluno.nome}")

# Opção 3
def ver_situacao():
    codigo_aluno = int(input("Digite o código do aluno: ")) - 1
    aluno = alunos[codigo_aluno] # Aluno("Daniel", [])
    aluno.situacao()

# Opção 4
def listar_alunos():
    if not alunos:
        print("Não há alunos cadastrados!")
        return
    
    for codigo_aluno, aluno in enumerate(alunos, start=1):
        print(f"\nCódigo aluno: {codigo_aluno}")
        aluno.exibir()

alunos = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")
    
    if opcao == "0":
        break
    elif opcao == "1":
        cadastrar_aluno()
    elif opcao == "2":
        lancar_nota()
    elif opcao == "3":
        ver_situacao()
    elif opcao == "4":
        listar_alunos()
    else:
        print("Opção Inválida")