from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.


class Manga(models.Model):
    MANGA_STATUS = (
        ('ON', 'ON GOING'),
        ('OFF', 'CANCELED'),
        ('FIN', 'FINISHED'),
        ('HIA', 'ON HIATUS')
    )

    nombreM = models.CharField('Nombre', max_length=100)
    autorM = models.CharField('Autor', max_length=100)
    manga_sta = models.CharField('Manga Status', max_length=3, choices=MANGA_STATUS)
    descriptionM = models.TextField('Descripción', max_length=1000, blank=True)
    generoM = models.CharField('Generos', max_length=250)
    rateM = models.FloatField('Rate', validators=[MinValueValidator(0.0), MaxValueValidator(5)])
    volumen = models.IntegerField('Volumenes', null=True)
    capitulos = models.IntegerField('Capitulos', null=True)


    objects= models.Manager()


    def __str__(self):
        return self.nombreM
