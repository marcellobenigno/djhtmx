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
