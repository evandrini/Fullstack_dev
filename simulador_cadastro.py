#SIMULADOR DE CADASTRO DE SENHA E INICIALIZAÇÃO DE CELULAR

senha_cadastrada = input("Cadastre sua senha: ")


print("Bem-vindo! Digite sua senha para iniciar o celular.")


for tentativa in range(3):
    senha_digitada = input("Digite sua senha: ")

    if senha_digitada == senha_cadastrada:
        print("Bem-vindo!")
        break
    else:
        tentativas_restantes = 2 - tentativa
        if tentativas_restantes > 0:
            print(f"Senha incorreta. Você tem {tentativas_restantes} tentativas até o bloqueio.")
        else:
            print("Sua senha foi bloqueada.")

