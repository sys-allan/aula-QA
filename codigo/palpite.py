numero_secreto = 17
acertou = False


while not acertou:
    palpite = int(input("digite um numero de 1 a 100: "))
    if palpite == numero_secreto:
        print("parabens! voce acertou o numero secreto!")
        acertou: True
    elif palpite < numero_secreto:
        print("o numero secreto e maior tente novamente!")
    else:
        print("o numero e menor tente novamente")

    print("fim")