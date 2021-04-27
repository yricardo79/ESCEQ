from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from registro.models import Equino, Raza

# Historia_Clinica
admin.site.register(Equino)


class RazaResosurce(resources.ModelResource):
    class Meta:
        model = Raza


class RazaAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ("id_raza", "nom_raza", "des_raza")
    search_fields = ("id_raza", "nom_raza")
    list_filter = ("id_raza", "nom_raza",)
    resource_class = RazaResosurce

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'


admin.site.register(Raza, RazaAdmin)
# admin.site.register(Post)

# class PruebaAdmin(admin.ModelAdmin):
#    list_display = ("prueba_campo")
# admin.site.register(Prueba) #, PruebaAdmin
# admin.site.register(Usuarios)


"""
class ComportamientoAdmin(admin.ModelAdmin):
    list_display = ("nom_comp", "des_comp")

class EquinoAdmin(admin.ModelAdmin):
    list_display = ("raza_id", "comp_id", "nom_equino", "fec_nacimiento", "adv_manejo", "sexo", "color")
    search_fields = ("id", "nom_equino")
    list_filter = ("fec_nacimiento",)
    date_hierarchy = "fec_nacimiento"

class DisciplinaDeportivaAdmin(admin.ModelAdmin):
    list_display = ("disciplina", "descripcion_dis")

class VeterinarioAdmin(admin.ModelAdmin):
    list_display = ("nombres_veterinario", "apellidos_veterinario", "correo_veterinario")

class Historia_ClinicaAdmin(admin.ModelAdmin):
    list_display = ("veterinario_id", "fecha_apertura", "estado", "observaciones")


#admin.site.register(Raza,RazaAdmin)
admin.site.register(Comportamiento, ComportamientoAdmin)
admin.site.register(Equino, EquinoAdmin)
admin.site.register(Disciplina_Deportiva, DisciplinaDeportivaAdmin)
admin.site.register(Veterinario, VeterinarioAdmin)
admin.site.register(Historia_Clinica, Historia_ClinicaAdmin)
"""
