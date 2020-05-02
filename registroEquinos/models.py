from django.db import models

"""
"""
class Usuarios(models.Model):
    usuario = models.CharField(max_length=10)
    contrasena = models.CharField(max_length=16)

    #video 15 pildoras informaticas
    def __str__(self):
        return 'El usuario es: %s y la contrasena es: %s' %(self.usuario, self.contrasena)


class Raza(models.Model):
    #id_raza = models.CharField(primary_key=True, max_length=100)
    nom_raza = models.CharField(max_length=255)
    des_raza = models.CharField(max_length=255)

    def __str__(self):
        return "La raza es: %s y su descripción es: %s" % (self.nom_raza, self.des_raza)

class Comportamiento(models.Model):
    #id_comp = models.CharField(primary_key=True, max_length=100)
    nom_comp = models.CharField(max_length=255)
    des_comp = models.CharField(max_length=255)


class Equino(models.Model):
    #id_chip = models.CharField(primary_key=True, max_length=100)
    raza_id = models.ForeignKey(Raza, null=True, blank=True, on_delete=models.CASCADE)
    comp_id = models.ForeignKey(Comportamiento, null=True, blank=True, on_delete=models.CASCADE)
    nom_equino = models.CharField(max_length=255)
    fec_nacimiento = models.DateField()
    adv_manejo = models.CharField(max_length=255)
    sexo = models.BooleanField()
    color = models.CharField(max_length=255)


class Disciplina_Deportiva(models.Model):
    #id_disciplina = models.CharField(primary_key=True, max_length=100)
    disciplina = models.CharField(max_length=255)
    descripcion_dis = models.CharField(max_length=255)


class Veterinario(models.Model):
    #id_veterinario = models.CharField(primary_key=True, max_length=100)
    nombres_veterinario = models.CharField(max_length=255)
    apellidos_veterinario = models.CharField(max_length=255)
    correo_veterinario = models.CharField(max_length=255)


class Historia_Clinica(models.Model):
    #id_equino_chip = models.CharField(primary_key=True, max_length=100)
    veterinario_id = models.ForeignKey(Veterinario, null=True, blank=True, on_delete=models.CASCADE)
    fecha_apertura = models.DateField()
    estado = models.CharField(max_length=255)
    observaciones = models.CharField(max_length=255)


class Prueba(models.Model):
    prueba_campo = models.CharField(max_length=255)
"""
"""