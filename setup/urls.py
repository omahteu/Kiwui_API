from django.contrib import admin
from django.urls import path, include
from contato.views import Contatoviewset
from inscritos.views import InscritoViewset
from rest_framework import routers


router = routers.DefaultRouter()
router.register('contatos', Contatoviewset, basename='contatos')
router.register('inscritos', InscritoViewset, basename='inscritos')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
