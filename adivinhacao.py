print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42

chute_str = int(input("Digite o seu numero: "))

print("Você digitou", chute_str)

if numero_secreto == chute_str:
    print("Você acertou!")
else:
    print("Você errou :(")

print("Fim do jogo!")
