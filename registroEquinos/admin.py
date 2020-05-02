from django.contrib import admin

# Register your models here.
from registroEquinos.models import Prueba, Usuarios, Raza, Comportamiento, Equino, Disciplina_Deportiva, Veterinario, \
    Historia_Clinica

#class PruebaAdmin(admin.ModelAdmin):
#    list_display = ("prueba_campo")
admin.site.register(Prueba) #, PruebaAdmin

admin.site.register(Usuarios)

class RazaAdmin(admin.ModelAdmin):
    list_display = ("nom_raza", "des_raza")

class ComportamientoAdmin(admin.ModelAdmin):
    list_display = ("nom_comp", "des_comp")

class EquinoAdmin(admin.ModelAdmin):
    list_display = ("raza_id", "comp_id", "nom_equino", "fec_nacimiento", "adv_manejo", "sexo", "color")

class DisciplinaDeportivaAdmin(admin.ModelAdmin):
    list_display = ("disciplina", "descripcion_dis")

class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ("nombres_veterinario", "apellidos_veterinario", "correo_veterinario")

class Historia_ClinicaAdmin(admin.ModelAdmin):
    list_display = ("veterinario_id", "fecha_apertura", "estado", "observaciones")

admin.site.register(Raza,RazaAdmin)
admin.site.register(Comportamiento, ComportamientoAdmin)
admin.site.register(Equino, EquinoAdmin)
admin.site.register(Disciplina_Deportiva, DisciplinaDeportivaAdmin)
admin.site.register(Veterinario, VeterinarioAdmin)
admin.site.register(Historia_Clinica, Historia_ClinicaAdmin)