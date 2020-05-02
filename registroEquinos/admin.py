from django.contrib import admin

# Register your models here.
from registroEquinos.models import Prueba, Usuarios, Raza, Comportamiento, Equino, Disciplina_Deportiva, Veterinario, \
    Historia_Clinica

admin.site.register(Prueba)
admin.site.register(Usuarios)
admin.site.register(Raza)
admin.site.register(Comportamiento)
admin.site.register(Equino)
admin.site.register(Disciplina_Deportiva)
admin.site.register(Veterinario)
admin.site.register(Historia_Clinica)

