from django.contrib import admin
from contato.models import Contato


class Contatos(admin.ModelAdmin):
    list_display = ('id', 'nome', 'email')


admin.site.register(Contato, Contatos)
