from django.db import models
# Create your models here.
class medicamentos(models.Model):
    id = models.AutoField(primary_key=True,verbose_name="Clave"),
    imagen=models.ImageField(null=True,upload_to="fotos",verbose_name="imagen del medicamento")
    clave=models.CharField(default='',max_length=20,verbose_name="clave del medicamento")
    nombre=models.CharField(default='',max_length=50,verbose_name="nombre del medicamento")
    cantidad=models.IntegerField(verbose_name="cantidad del medicamento")
    fecha_de_caducidad=models.DateField(verbose_name="fecha de caducidad")
    descripcion=models.TextField(default='',verbose_name="descripcion")
    disponibilidad=models.TextField(default='',verbose_name="disponibilidad")
    created = models.DateTimeField(auto_now_add=True)  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "medicamento"
        verbose_name_plural = "medicamentos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre 

class salida_medicamento(models.Model):
    nombre_paciente=models.CharField(default='',max_length=50,verbose_name="Nombre del paciente")
    medicamento=models.ForeignKey(medicamentos, verbose_name=("Medicamento"), on_delete=models.CASCADE)
    cantidad_suministrada=models.IntegerField(verbose_name="cantidad de medicamento suministrado")
    fecha_suministrada=models.DateField(verbose_name="fecha suministrada")
    created = models.DateTimeField(auto_now_add=True)  # Fecha y tiempo
    updated = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "salidamedicamento"
        verbose_name_plural = "salidamedicamentos"
        ordering = ["created"]

    def __str__(self):
        return self.nombre_paciente