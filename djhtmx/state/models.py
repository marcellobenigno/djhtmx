from django.db import models


class State(models.Model):
    initials = models.CharField('Sigla', max_length=2)
    name = models.CharField('Nome', max_length=50)
    region = models.CharField('Região', max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Estado"
        verbose_name_plural = "Estados"
        ordering = ("name",)


class Municipality(models.Model):
    state = models.ForeignKey('State', verbose_name='estado', related_name='municipio', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=50)
    cod_ibge_m = models.IntegerField('Cód. IBGE')
    slug = models.SlugField('Slug', max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Município"
        verbose_name_plural = "Municípios"
        ordering = ("name",)
