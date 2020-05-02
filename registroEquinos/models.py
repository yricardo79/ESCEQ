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
    nom_raza = models.CharField(max_length=255, verbose_name="Nombre raza")
    des_raza = models.CharField(max_length=255, verbose_name="Descripción")

    def __str__(self):
        return "La raza es: %s y su descripción es: %s" % (self.nom_raza, self.des_raza)


class Comportamiento(models.Model):
    #id_comp = models.CharField(primary_key=True, max_length=100)
    nom_comp = models.CharField(max_length=255, verbose_name="Nombre")
    des_comp = models.CharField(max_length=255, verbose_name="Descripción")

    def __str__(self):
        return " : %s : %s" % (self.nom_comp, self.des_comp)


class Equino(models.Model):
    #id_chip = models.CharField(primary_key=True, max_length=100)
    raza_id = models.ForeignKey(Raza, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Raza")
    comp_id = models.ForeignKey(Comportamiento, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Comp")
    nom_equino = models.CharField(max_length=255, verbose_name="Nombre")
    fec_nacimiento = models.DateField(verbose_name="Fecha nacimiento")
    adv_manejo = models.CharField(max_length=255, verbose_name="Adv Manejo")
    sexo = models.BooleanField(verbose_name="Sexo")
    color = models.CharField(max_length=255, verbose_name="Color")


class Disciplina_Deportiva(models.Model):
    #id_disciplina = models.CharField(primary_key=True, max_length=100)
    disciplina = models.CharField(max_length=255, verbose_name="Disciplina")
    descripcion_dis = models.CharField(max_length=255, verbose_name="Descripción")


class Veterinario(models.Model):
    #id_veterinario = models.CharField(primary_key=True, max_length=100)
    nombres_veterinario = models.CharField(max_length=255, verbose_name="Nombres")
    apellidos_veterinario = models.CharField(max_length=255, verbose_name="Apellidos")
    correo_veterinario = models.CharField(max_length=255, verbose_name="Correo veterinario")


class Historia_Clinica(models.Model):
    #id_equino_chip = models.CharField(primary_key=True, max_length=100)
    veterinario_id = models.ForeignKey(Veterinario, null=True, blank=True, on_delete=models.CASCADE, verbose_name="Iden. veterinario")
    fecha_apertura = models.DateField(verbose_name="Fecha apertura")
    estado = models.CharField(max_length=255, verbose_name="Estado")
    observaciones = models.CharField(max_length=255, verbose_name="Observaciones")


class Prueba(models.Model):
    prueba_campo = models.CharField(max_length=255, verbose_name="Campo de prueba")

"""
"""