from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

from escola.models import Aluno, Curso, Matricula


@admin.register(Aluno)
class Alunos(admin.ModelAdmin):
    list_display = ["id", "nome", "rg", "cpf", "data_nascimento"]
    list_display_links = ["id", "nome"]
    search_fields = ["nome"]
    list_per_page = 20


@admin.register(Curso)
class Cursos(admin.ModelAdmin):
    list_display = ["id", "codigo_curso", "descricao", "nivel"]
    list_display_links = ["id", "codigo_curso", "nivel"]
    search_fields = ["codigo_curso"]
    list_per_page = 20


@admin.register(Matricula)
class Matriculas(admin.ModelAdmin):
    list_display = ["id", "aluno", "curso", "periodo"]
    list_display_links = ["id"]


# admin.site.register(Session)
@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ["session_key", "expire_date", "get_user"]

    def get_user(self, request):
        user_id = request.get_decoded()['_auth_user_id']
        user = User.objects.get(pk=user_id)
        return user.username

    get_user.short_description = "Logged user"