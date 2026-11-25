import pandas as pd

dados = {
    'nome': ["joao","marta","ary","matheus","michele"],
    'idade': [51,37,23,24,33],
    'cidade': ["recife","salvador","sao paulo","manaus", "montes claros"]
}

conteiner = pd.DataFrame(dados)

print(40*"=")
print("com import pandas")
print(conteiner)
print(40*"=")

print(conteiner[conteiner["cidade"] == ("sao paulo")])


