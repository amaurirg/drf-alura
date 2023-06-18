from rest_framework import viewsets, status
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

# from rest_framework.authentication import BasicAuthentication
# from rest_framework.permissions import IsAuthenticated

from escola.models import Aluno, Curso, Matricula
from escola.serializer import AlunoSerializer, CursoSerializer, MatriculaSerializer, ListaMatriculasAlunoSerializer, \
    ListaMatriculadosPorCursoSerializer, AlunoSerializerV2


class AlunosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os alunos """
    queryset = Aluno.objects.all()
    # authentication_classes = [BasicAuthentication]
    # permission_classes = [IsAuthenticated]
    def get_serializer_class(self):
        if self.request.version == "v2":
            return AlunoSerializerV2
        return AlunoSerializer


class CursosViewSet(viewsets.ModelViewSet):
    """ Exibindo todos os cursos """
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response = Response(serializer.data, status=status.HTTP_201_CREATED)
            # Serve para quando criar um novo curso, aparecer o Location na aba network -> cabeçalho
            # O Location serve para mostrar o link do novo curso criado. Ex: http://127.0.0.1:8000/cursos/5
            response["Location"] = f"{request.build_absolute_uri()}{serializer.data['id']}"
            return response


class MatriculasViewSet(viewsets.ModelViewSet):
    """ Exibindo todas as matrículas """
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer
    http_method_names = ["get", "post"]


class ListaMatriculasAluno(ListAPIView):
    """ Listando matrículas de um aluno """
    def get_queryset(self):
        queryset = Matricula.objects.filter(aluno_id=self.kwargs['pk'])
        return queryset
    serializer_class = ListaMatriculasAlunoSerializer


class ListaMatriculadosPorCurso(ListAPIView):
    """ Listando alunos matriculados em um curso """
    def get_queryset(self):
        queryset = Matricula.objects.filter(curso_id=self.kwargs["pk"])
        return queryset
    serializer_class = ListaMatriculadosPorCursoSerializer
