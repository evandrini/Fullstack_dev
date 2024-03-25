alunos = {}

while True:
    print("Selecione uma opção: ")
    print("1. Adicionar aluno")
    print("2. Remover aluno")
    print("3. Visualizar todos os alunos")
    print("4. Sair")

    opcao = input("Opção: ")

    if opcao == '1':
        nome = input("Digite o nome do aluno: ")
        matricula = input("Digite o número de matrícula do aluno: ")
        alunos[matricula] = nome
        print("Aluno adicionado com sucesso!")

    elif opcao == '2':
        if len(alunos) == 0:
            print("Nenhum aluno registrado.")
        else:
            matricula = input("Digite o número de matrícula do aluno a ser removido: ")
            if matricula in alunos:
                del alunos[matricula]
                print("Aluno removido com sucesso!")
            else:
                print("Aluno não encontrado.")

    elif opcao == '3':
        if len(alunos) == 0:
            print("Nenhum aluno registrado.")
        else:
            print("Lista de alunos: ")
            for matricula, nome in alunos.items():
                print(f"Matrícula: {matricula}, Nome: {nome}")

    elif opcao == '4':
        print("Até logo!")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")