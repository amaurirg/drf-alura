from rest_framework import serializers

from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ["nome", "rg", "cpf", "data_nascimento"]


class AlunoSerializerV2(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = "__all__"


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = "__all__"


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []  # traz todos os campos também


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(source="curso.descricao")
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ["curso", "periodo"]

    def get_periodo(self, obj):
        return obj.get_periodo_display()


class ListaMatriculadosPorCursoSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source="aluno.nome")

    class Meta:
        model = Matricula
        fields = ["aluno_nome"]
