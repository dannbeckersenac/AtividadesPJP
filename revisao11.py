usuario_correto = "admin"
senha_correta = "1234"
usuario = ""
senha = ""

while usuario != usuario_correto or senha != senha_correta:
    usuario = input("Digite o nome de usuário: ") # usuario
    senha = input("Digite a senha: ") # 1234

    if usuario != usuario_correto or senha != senha_correta:
        print("Usuário e senha incorretos! Tente novamente")
    else:
        print("Acesso permitido!")