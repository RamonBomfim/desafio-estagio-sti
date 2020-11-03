from django.db import models
from apps.usuario.models import User


class Fishing(models.Model):
    fisherman_name = models.ForeignKey(User, on_delete=models.CASCADE,
                                       related_name='Capitão', verbose_name='Capitão')
    immediate = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Imediato', verbose_name='Imediato')
    pilot = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Piloto', verbose_name='Piloto')
    friend = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Amigo', verbose_name='Amigo',
                               null=True, blank=True)
    fishing_day = models.DateField('Data da pesca')
    fishing_hour = models.TimeField('Horário da pesca')
    localization = models.CharField('Local da pesca', max_length=100)

    class Meta:
        verbose_name = 'Fishing'
        verbose_name_plural = 'Fisheries'
        ordering = ['fishing_day']

    def __str__(self):
        return self.fisherman_name.name
