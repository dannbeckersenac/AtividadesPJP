def exibir_menu():
    print("\n===================")
    print("Menu:")
    print("1 - Adicionar uma tarefa.")
    print("2 - Visualizar tarefas.")
    print("3 - Remover tarefas.")
    print("0 - Sair.")
    print("===================")

def adicionar_tarefa(tarefas):
    tarefa = input("Digite a tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada com sucesso!")

def listar_tarefas(tarefas):
    if not tarefas:
        print("Não há tarefas para exibir!")
    else:
        for posicao_tarefa, tarefa in enumerate(tarefas, start=1):
            print(f"{posicao_tarefa} - {tarefa}")

def remover_tarefa(tarefas):
    if not tarefas:
        print("Não há tarefas para remover!")
    else:
        tarefa = int(input("Digite o número da tarefa que deseja remover: "))
        tarefa = tarefa - 1
        tarefa_removida = tarefas.pop(tarefa)
        print(f"Tarefa removida: {tarefa_removida}")

tarefas = []

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    # Faça os if/elif/else aqui!
    if opcao == "0":
        print("Encerrando o programa...")
        break
    elif opcao == "1":
        adicionar_tarefa(tarefas)
    elif opcao == "2":
        listar_tarefas(tarefas)
    elif opcao == "3":
        remover_tarefa(tarefas)
    else:
        print("Opção inválida!")