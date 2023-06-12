import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
from validate_docbr import CPF
from random import randrange, choice
from clientes.models import Cliente


def criando_pessoas(quantidade_de_pessoas):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(quantidade_de_pessoas):
        cpf = CPF()
        nome = fake.name()
        email = f"{nome.lower()}@{fake.free_email_domain()}".replace(' ', '')
        cpf = cpf.generate()
        rg = f"{randrange(10, 99)}{randrange(100, 999)}{randrange(100, 999)}{randrange(0, 9)}"
        celular = f"{randrange(10, 21)} 9{randrange(4000, 9999)}-{randrange(4000, 9999)}"
        ativo = choice([True, False])
        p = Cliente(nome=nome, email=email, cpf=cpf, rg=rg, celular=celular, ativo=ativo)
        p.save()


criando_pessoas(50)
print("Pessoas criadas com sucesso!")
