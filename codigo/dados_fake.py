
from faker import Faker


fake = Faker("pt_br")

dados = {
    'nomes': [],
    'idade': [],
    'cidade':[]
}

nome = fake.name()

dados['nomes'].append(nome)

print(dados)