
nome = ""
idade = ""
habilitaçao = ""


print("ola, bem vindo. vem tirar sua CNH")

nome = input("digite o seu nome: ")
print("seja bem vindo!: " ,nome)

idade = int(input("digite a sua idade!: "))

if idade >= 18:
    print("voce ja pode possuir sua CHN ")

elif idade == 17: 
    print("falta poupo para garantir ")

else: 
    print("nao pode possuir sua CNH. tenha paciencia")

