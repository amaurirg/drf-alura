from rest_framework import serializers
from clientes.models import Cliente
from clientes import validators

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'

    def validate(self, data):
        if not validators.nome(data["nome"]):
            raise serializers.ValidationError({"nome": "O nome não deve conter dígitos"})
        if not validators.cpf(data["cpf"]):
            raise serializers.ValidationError({"cpf": "CPF inválido"})
        if not validators.rg(data["rg"]):
            raise serializers.ValidationError({"rg": "O RG deve ter 9 dígitos"})
        if not validators.celular(data["celular"]):
            raise serializers.ValidationError({"celular": "O celular deve ter 11 dígitos"})
        return data


    # def validate_nome(self, nome):
    #     if not nome.isalpha():
    #         raise serializers.ValidationError("O nome não deve conter dígitos")
    #     return nome
    #
    # def validate_cpf(self, cpf):
    #     if not len(cpf) == 11:
    #         raise serializers.ValidationError("O CPF deve ter 11 dígitos")
    #     return cpf
    #
    # def validate_celular(self, celular):
    #     if not len(celular) == 11:
    #         raise serializers.ValidationError("O celular deve ter 11 dígitos")
    #     return celular
