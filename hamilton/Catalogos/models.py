from django.db import models

# Create your models here.
class SepoMex(models.Model):
    id= models.AutoField(primary_key=True)
    d_codigo = models.CharField(max_length=8)
    d_asenta = models.CharField(max_length=255)
    d_tipo_asenta = models.CharField(max_length=100)
    D_mnpio = models.CharField(max_length=255)
    d_estado = models.CharField(max_length=100)
    d_ciudad = models.CharField(max_length=255, blank=True, null=True)
    d_CP = models.CharField(max_length=8, blank=True, null=True)
    c_estado = models.IntegerField(blank=True, null=True)
    c_oficina = models.IntegerField(blank=True, null=True)
    c_CP = models.IntegerField(blank=True, null=True)
    c_tipo_asenta = models.IntegerField(blank=True, null=True)
    c_mnpio = models.IntegerField(blank=True, null=True)
    id_asenta_cpcons = models.IntegerField(blank=True, null=True)
    d_zona = models.CharField(max_length=100, blank=True, null=True)
    c_cve_ciudad = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 'cat_sepomex'

    def __str__(self):
        return f"{self.d_asenta} | {self.d_mnpio} | {self.d_estado}"


class Opciones(models.Model):
    numero = models.IntegerField(null=True, blank=True)
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name='descripcion')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_opciones'
    
    def __str__(self):
        return f"{self.numero} | {self.descripcion} | {self.activo}"


class Categorias(models.Model):
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name='descripcion')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_categoria'
    
    def __str__(self):
        return f"{self.descripcion} | {self.activo}"


class Preguntas(models.Model):
    orden = models.IntegerField(null=True, blank=True)
    pregunta = models.CharField(max_length=150, blank=True, null=True, verbose_name='pregunta')
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name='descripcion')
    categoria = models.ForeignKey(Categorias, on_delete=models.CASCADE, related_name='preguntas')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_preguntas'
    
    def __str__(self):
        return f"{self.orden} | {self.descripcion} | {self.activo}"


class Generos(models.Model):
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name='descripcion')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_generos'
    
    def __str__(self):
        return f"{self.descripcion} | {self.activo}"


class Edades(models.Model):
    descripcion = models.CharField(max_length=150, blank=True, null=True, verbose_name='descripcion')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_edades'
    
    def __str__(self):
        return f"{self.descripcion} | {self.activo}"

class Escolaridad(models.Model):
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name='descripcion')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_escolaridad'
    
    def __str__(self):
        return f"{self.descripcion} | {self.activo}"

class Ocupacion(models.Model):
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name='descripcion')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_ocupacion'
    
    def __str__(self):
        return f"{self.descripcion} | {self.activo}"

class Parentesco(models.Model):
    descripcion = models.CharField(max_length=250, blank=True, null=True, verbose_name='descripcion')
    activo = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'cat_parentesco'
    
    def __str__(self):
        return f"{self.descripcion} | {self.activo}"