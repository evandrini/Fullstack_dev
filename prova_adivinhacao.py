# Escreva um programa que peça ao usuário para adivinhar um número que você deverá escolher com antecedência até que ele acerte. 
# Para ajudar o usuário, o programa deve informar se o número é maior ou menor que o número a ser adivinhado. 
# Ao final, imprima o número adivinhado e a quantidade de tentativas. While e break

from random import randint
numero_aleatorio = randint(1,100)
print("----- Jogo de Adivinhação. Tente adivinhar o número aleatório! -----")
numero_usuario = int(input("Digite um número: "))
tentativas = 0

while True:
    if numero_usuario == numero_aleatorio:
        print(f"Você acertou apos tentar {tentativas} vezes!")       
        break

    elif numero_usuario < numero_aleatorio:
        print(f"Você tentou digitar o número: {numero_usuario} é menor. Tente novamente!")
        tentativas +=1
        numero_usuario = int(input("Tente acertar o número: "))

    elif numero_usuario > numero_aleatorio:
        print(f"Você tentou digitar o número: {numero_usuario} é maior. Tente novamente!")
        tentativas +=1
        numero_usuario = int(input("Tente acertar o número: "))