from django.contrib import admin
from inscritos.models import Inscrito


class Inscritos(admin.ModelAdmin):
    list_display = ('id', 'email')


admin.site.register(Inscrito, Inscritos)

