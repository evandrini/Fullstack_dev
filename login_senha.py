email_cadastrado = "evandro@gmail.com"
senha_cadastrada = "123456"

while True:
    validacao_email = input("Digite seu e-mail: ")
    validacao_senha = input("Digite sua senha: ")
    
    if validacao_email == email_cadastrado and validacao_senha == senha_cadastrada:

        print("Login e senha feito com sucesso!")

    else:
        print("Login ou senha incorretos. Tente novamente")
