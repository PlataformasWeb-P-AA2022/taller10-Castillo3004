from django.db import models

# Create your models here.

class Parroquia(models.Model):
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30)

    def __str__(self):
        return "%s %s" % (self.nombre, self.tipo)


class Barrio(models.Model):
    nombre = models.CharField(max_length=30)
    nroViviendas = models.IntegerField(verbose_name="Numero Viviendas")
    nroParques = models.IntegerField(verbose_name="Numero Parques")
    nroEdificios = models.IntegerField(verbose_name="Numero Edificios")
    parroquia = models.ForeignKey(Parroquia, on_delete= models.CASCADE, 
            related_name="los_barrios")

    def __str__(self):
        return  "%s %s %s %s" % (self.nombre, 
                self.nroViviendas, 
                self.nroParques,
                self.nroEdificios)
