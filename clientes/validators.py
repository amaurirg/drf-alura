from validate_docbr import CPF


def nome(nome):
    return nome.isalpha()


def cpf(cpf_number):
    cpf = CPF()
    return cpf.validate(cpf_number)


def rg(rg):
    return len(rg) == 9


def celular(celular):
    return len(celular) == 11
