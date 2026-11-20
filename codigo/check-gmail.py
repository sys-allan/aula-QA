

nome = input("Digite o seu nome: ")
gmail_usuario = input(f"{nome}, digite o seu GMAIL: ")
verificacao = input(f"{nome}, verifique o seu GMAIL: ")

print(f"Vamos checar no nosso sistema, {nome}...")

if gmail_usuario == verificacao:
    print("Cadastrado com sucesso!")
    print("Bem-vindo ao Bitrix!")
else:
    print("Os e-mails não coincidem. Verifique novamente!")

# gmail teste: afifa5139@uorak.com