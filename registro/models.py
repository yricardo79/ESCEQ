from django.db import models
from django.db.models import Model


# Valores llaves selects
class Valores_Selects_Vario(models.Model):
    sexo_equino = models.CharField(max_length=255, verbose_name="Sexo")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Valores_Selects_Vario'
        verbose_name_plural = 'Valores_Selects_Varios'
        db_table = 'Valores_Selects_Vario'
        ordering = ['-id']

    def __str__(self):
        return "%s " % (self.sexo_equino)


class Veterinario(models.Model):
    cedula = models.IntegerField(primary_key=True, verbose_name="Cedula", unique=True)
    nombres_veterinario = models.CharField(max_length=255, verbose_name="Nombres")
    apellidos_veterinario = models.CharField(max_length=255, verbose_name="Apellidos")
    fecha_nac_veterinario = models.DateField(verbose_name="Fecha de nacimiento")
    correo_veterinario = models.EmailField(blank=False, verbose_name="Correo veterinario")
    foto_vet = models.ImageField(upload_to='veterinarios', null=True)

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Veterinario'
        verbose_name_plural = 'Veterinarios'
        db_table = 'veterinario'
        ordering = ['-cedula']

    def __str__(self):
        return '{} {} {}'.format(self.cedula, self.nombres_veterinario, self.apellidos_veterinario)


class Comportamiento(models.Model):
    id_comp = models.AutoField(primary_key=True, verbose_name="Identificador de comportamiento", unique=True)
    nombre_com = models.CharField(max_length=255, verbose_name="Nombre comportamiento")
    descripcion_com = models.CharField(max_length=255, verbose_name="Descripción comportamiento")

    def __str__(self):
        return self.id_comp.chip

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Comportamiento'
        verbose_name_plural = 'Comportamientos'
        db_table = 'comportamiento'
        ordering = ['-id_comp']

    def __str__(self):
        return "%s " % (self.nombre_com)


class Raza(models.Model):
    id_raza = models.AutoField(primary_key=True, verbose_name="Identificador Raza")
    nom_raza = models.CharField(max_length=255, verbose_name="Nombre raza")
    des_raza = models.CharField(max_length=255, verbose_name="Descripción")

    def __str__(self):
        return self.id_raza.chip

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Raza'
        verbose_name_plural = 'Razas'
        db_table = 'raza'
        ordering = ['-id_raza']

    def __str__(self):
        return "%s " % (self.nom_raza)


class Comps_Nutricional(models.Model):
    id_comp = models.AutoField(primary_key=True, verbose_name="Identificador compuesto nutricional", unique=True)
    comp_nutricional = models.CharField(max_length=255, verbose_name="Comps nutricionales")
    tipo_componente = models.CharField(max_length=255, verbose_name="Tipo componente")
    observaciones = models.CharField(max_length=255, verbose_name="Observaciones")

    def __str__(self):
        return self.id_raza.chip

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Comps_Nutricional'
        verbose_name_plural = 'Comps_Nutricionales'
        db_table = 'comps_nutricional'
        ordering = ['-id_comp']

    def __str__(self):
        return "%s " % (self.comp_nutricional)


class Disciplina_Deportiva(models.Model):
    id_dis_dep = models.AutoField(primary_key=True, verbose_name="Identificador disciplina deportiva", unique=True)
    nombre_dis_dep = models.CharField(max_length=255, verbose_name="Nombre disciplina")
    descripcion_dis_dep = models.CharField(max_length=255, verbose_name="Descripción disciplina")

    def __str__(self):
        return self.id_dis_dep.chip_equ_disc

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Disciplina_Deportiva'
        verbose_name_plural = 'Disciplina_Deportivas'
        db_table = 'disciplina_deportiva'
        ordering = ['-id_dis_dep']

    def __str__(self):
        return "%s " % (self.nombre_dis_dep)


class Equ_Disc(models.Model):
    chip_equ_disc = models.AutoField(primary_key=True, verbose_name="Id Equino disciplina", unique=True)
    disciplina_id = models.ForeignKey(Disciplina_Deportiva, on_delete=models.CASCADE)
    exigencia = models.CharField(max_length=255, verbose_name="Exigencia")

    def __str__(self):
        return self.chip_equ_disc.chip

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Equ_Disc'
        verbose_name_plural = 'Equ_Discs'
        db_table = 'equ_disc'
        ordering = ['-chip_equ_disc']

    def __str__(self):
        return "%s " % (self.disciplina_id)


class Equino(models.Model):
    chip = models.IntegerField(primary_key=True, verbose_name="Chip del equino", unique=True)
    nom_equino = models.CharField(max_length=255, verbose_name="Nombre del equino")
    fec_nacimiento = models.DateField(verbose_name="Fecha de nacimiento")
    adv_manejo = models.TextField(verbose_name="adv_manejo")
    sexo = models.ForeignKey(Valores_Selects_Vario, on_delete=models.CASCADE)
    color = models.CharField(max_length=255, verbose_name="Color")
    raza = models.ForeignKey(Raza, on_delete=models.CASCADE)
    comportamiento = models.ForeignKey(Comportamiento, on_delete=models.CASCADE)
    disciplia = models.ForeignKey(Equ_Disc, on_delete=models.CASCADE)

    def __str__(self):
        return self.chip

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Equino'
        verbose_name_plural = 'Equinos'
        ordering = ['-chip']

    def __str__(self):
        return '{}'.format(self.chip)


class Historia_Clinica(models.Model):
    id_historia = models.AutoField(primary_key=True, verbose_name="Id Historia clinica", unique=True)
    equino_chip = models.ForeignKey(Equino, on_delete=models.CASCADE, unique=True)  # ,
    cedula_vet = models.ForeignKey(Veterinario, on_delete=models.CASCADE, verbose_name="FK Identificador veterinario")
    fecha_apertura = models.DateField()
    estado = models.CharField(max_length=50, verbose_name="Estado")
    observaciones = models.TextField(verbose_name="Observaciones")

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Historia_Clinica'
        verbose_name_plural = 'Historia_Clinicas'
        db_table = 'historia_clinica'
        ordering = ['-id_historia']

    def __str__(self):
        return "%s - %s" % (self.id_historia, self.equino_chip)


class Consulta(models.Model):
    id_consulta = models.AutoField(verbose_name='Id consulta', primary_key=True)
    chip_equino = models.ForeignKey(Equino, on_delete=models.CASCADE)
    fecha = models.DateField(verbose_name="Fecha")
    historia_clinica = models.ForeignKey(Historia_Clinica, on_delete=models.CASCADE)
    frec_cardiaca = models.FloatField(verbose_name="Frecuencia cardiaca")
    frec_respiratoria = models.FloatField(verbose_name="Frecuencia respiratoria")
    pulso = models.CharField(max_length=255, verbose_name="Pulso")
    temperatura = models.FloatField(verbose_name="Temperatura")
    est_hidratacion = models.CharField(max_length=255, verbose_name="Estado hidratación")
    porc_deshidrat = models.FloatField(verbose_name="Porcentaje deshidratación")
    peso = models.FloatField(verbose_name="Peso")
    conjuntival = models.CharField(max_length=255, verbose_name="Conjuntival")
    oral = models.CharField(max_length=255, verbose_name="Oral")
    vulva_prepucio = models.CharField(max_length=255, verbose_name="Vulva o prepucio")
    rectal = models.CharField(max_length=255, verbose_name="Rectal")
    ojos = models.TextField(verbose_name="Ojos")  # blank=True
    oidos = models.TextField(verbose_name="Oidos")  # blank=True
    nod_linfaticos = models.TextField(verbose_name="Nod linfaticos")  # blank=True

    def __str__(self):
        return self.id_consulta

    class Meta:
        verbose_name = 'Consulta'
        verbose_name_plural = 'Consultas'
        db_table = 'consulta'
        ordering = ['-id_consulta']


class Dieta(models.Model):
    id_dieta = models.AutoField(primary_key=True, verbose_name="Id chip dieta", unique=True)
    # chip_equino = models.ManyToManyField(Equino)
    chip_equino = models.ForeignKey(Equino, on_delete=models.CASCADE, unique=True)
    nombre_dieta = models.CharField(max_length=255, verbose_name="Nombre de la dieta")
    id_fecha = models.DateField(verbose_name="Id fecha", unique=True)
    comps_nutricionales_id = models.ForeignKey(Comps_Nutricional, on_delete=models.CASCADE)
    veterinario_cedula = models.ForeignKey(Veterinario, on_delete=models.CASCADE)
    estado = models.CharField(max_length=255, verbose_name="Estado")
    id_des_conc = models.IntegerField(verbose_name="id_des_conc")
    cant_des_conc = models.FloatField(verbose_name="cant_des_conc")
    id_alm_con = models.IntegerField(verbose_name="id_alm_con")
    cant_alm_conc = models.FloatField(verbose_name="cant_alm_conc")
    id_com_conc = models.IntegerField(verbose_name="id_com_conc")
    cant_com_conc = models.FloatField(verbose_name="cant_com_conc")
    id_des_forraje = models.IntegerField(verbose_name="id_des_forraje")
    cant_des_forraje = models.FloatField(verbose_name="cant_des_forraje")
    id_alm_forraje = models.IntegerField(verbose_name="id_alm_forraje")
    cant_alm_forraje = models.FloatField(verbose_name="cant_alm_forraje")
    id_des_suple = models.IntegerField(verbose_name="id_des_suple")
    cant_des_suple = models.FloatField(verbose_name="cant_des_suple")
    id_alm_suple = models.IntegerField(verbose_name="id_alm_suple")
    cant_alm_suple = models.FloatField(verbose_name="cant_alm_suple")
    id_com_suple = models.IntegerField(verbose_name="id_com_suple")
    cant_com_suple = models.IntegerField(verbose_name="cant_com_suple")
    hora_des_conc = models.TimeField(verbose_name="hora_des_conc")
    hora_des_forraje = models.TimeField(verbose_name="hora_des_forraje")
    hora_des_suple = models.TimeField(verbose_name="hora_des_suple")
    hora_alm_suple = models.TimeField(verbose_name="hora_alm_suple")
    hora_alm_forraje = models.TimeField(verbose_name="hora_alm_forraje")
    hora_alm_conc = models.TimeField(verbose_name="hora_alm_conc")
    hora_com_suple = models.TimeField(verbose_name="hora_com_suple")
    hora_com_forraje = models.TimeField(verbose_name="hora_com_forraje")

    def __str__(self):
        return self.nombre_dieta

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Dieta'
        verbose_name_plural = 'Dietas'
        db_table = 'dieta'
        ordering = ['-id_dieta']


class Foto_Equino(models.Model):
    equino = models.ForeignKey(Equino, on_delete=models.CASCADE)
    # foto = models.ImageField(upload_to='equino/%Y/%m/%d')
    foto = models.ImageField(upload_to='equino/%Y/%m/%d', null=True, blank=True)

    def __str__(self):
        return self.id

    def __unicode__(self, ):
        return str(self.image)

    class Meta:
        verbose_name = 'Foto_Equino'
        verbose_name_plural = 'Foto_Equinos'
        db_table = 'foto_equino'
        ordering = ['-id']

    def __str__(self):
        return '{} {}'.format(self.id, self.equino)


# Yeimmy Ricardo
extras = [("1", "Si"), ("0", "No")]

SELECION = [('1', 'Si'), ('0', 'No')]


# Variables clinicas y de manejo que no estan en el modeloG
class Variables(models.Model):
    id_var = models.AutoField(primary_key=True)
    chip = models.ForeignKey(Equino, on_delete=models.CASCADE, verbose_name="FK Identificador Equino", null=True)
    fecha_registro = models.DateField(auto_now=True)
    claudicacion = models.IntegerField(verbose_name="Hay claudicacion", choices=SELECION)
    grado_claudi = models.IntegerField(verbose_name="Grado de claudicacion")
    presencia_sangre = models.IntegerField(verbose_name="Presencia en sangre", choices=SELECION)
    olleres = models.IntegerField(verbose_name="Olleres", choices=SELECION)
    boca = models.IntegerField(verbose_name="Boca", choices=SELECION)
    heridas_sangrantes = models.IntegerField(verbose_name="Heridas sangrantes", choices=SELECION)
    evidencia_fat_sud = models.IntegerField(verbose_name="Evidencia fatiga o sudacion", choices=SELECION)
    grano = models.IntegerField(verbose_name="Grano kilogramos")
    forraje = models.IntegerField(verbose_name="Forraje kilogramos")
    suplemento = models.IntegerField(verbose_name="Sumplemento", choices=SELECION)
    sup_oral = models.IntegerField(verbose_name="Suplemento oral", choices=SELECION)
    sup_intravenoso = models.IntegerField(verbose_name="Suplemento intravenoso", choices=SELECION)
    dieta_veces_dia = models.IntegerField(verbose_name="Dieta veces al dia")
    dieta_horarios = models.IntegerField(verbose_name="Dieta horarios")
    calentamiento_previo = models.IntegerField(verbose_name="Calentamiento previo", choices=SELECION)
    hora_calentamiento = models.IntegerField(verbose_name="Hora calentamiento")
    minuto_calentamiento = models.IntegerField(verbose_name="Minuto calentamiento")
    trabajo_cantidad_horas = models.IntegerField(verbose_name="Trabajo cantidad de horas")
    trabajo_cantidad_diaria = models.IntegerField(verbose_name="Trabajo cantidad diario")
    trabajo_cantidad_semanal = models.IntegerField(verbose_name="Trabajo cantidad semanal")
    trabajo_potrero = models.IntegerField(verbose_name="Trabajo potrero", choices=SELECION)
    trabajo_caminador = models.IntegerField(verbose_name="Trabajo caminador", choices=SELECION)
    tiempo_pot_cam_horas = models.IntegerField(verbose_name="Tiempo potrero o caminador horas")
    tiempo_pot_cam_mins = models.IntegerField(verbose_name="Tiempo potrero o caminador minutos")
    puntaje = models.FloatField(verbose_name="Puntaje predecido")

    def __str__(self):
        return self.nombre_dieta

    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Variable'
        verbose_name_plural = 'Variables'
        db_table = 'variables'
        ordering = ['-fecha_registro']

# class Cargue_Modelo(models.Model):
#     id_cargue = models.AutoField(primary_key=True)
#     ruta = models.CharField(max_length=255, verbose_name="Ruta archivo")
#     fecha_cargue = models.DateTimeField(auto_now=True)
#
#     def __str__(self):
#         return self.nombre_dieta
#
#     def toJSON(self):
#         item = model_to_dict(self)
#         return item
#
#     class Meta:
#         verbose_name = 'Cargue_Modelo'
#         verbose_name_plural = 'Cargue_Modelos'
#         db_table = 'cargue_modelo'
#         ordering = ['-chip']
