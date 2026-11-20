
nome = input("digite o seu nome: ")
gmail_usuario = int(input(f"{nome}digite o seu GMAIL: "))
verificacao = int(input(f"{nome}, verefique o seu GMAIL!: ")) 
print(f"vamos checar no nosso sistema {nome}")


if gmail_usuario == verificacao:
    print("cadastrado com sucesso!")
elif gmail_usuario:
    print("verefica novamente!")
else:
    print("passou na verificaçao!")

print("bem vindo ao bitrix")