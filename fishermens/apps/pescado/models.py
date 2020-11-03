from django.db import models
from apps.usuario.models import User


class RankingWeight(models.Model):
    fisherman = models.ForeignKey(User, on_delete=models.CASCADE)
    fish_species = models.CharField('Espécie do peixe', max_length=30)
    fish_weight = models.DecimalField('Massa em kg', max_digits=6, decimal_places=2)
    fish_size = models.DecimalField('Tamanho do peixe em cm', max_digits=6, decimal_places=2, default=0)
    image = models.ImageField('Foto do peixe', upload_to='fish_images')

    class Meta:
        verbose_name = 'Weight Ranking'
        verbose_name_plural = 'Weight Ranking'
        ordering = ['-fish_weight']

    def __str__(self):
        return self.fisherman.name


class RankingAmount(models.Model):
    fisherman = models.ForeignKey(User, on_delete=models.CASCADE)
    fish_species = models.CharField('Espécie do peixe', max_length=30)
    fish_amount = models.IntegerField('Quantidade pescada')
    image = models.ImageField('Foto do peixe', upload_to='fish_images')

    class Meta:
        verbose_name = 'Amount Ranking'
        verbose_name_plural = 'Amount Ranking'
        ordering = ['-fish_amount']

    def __str__(self):
        return self.fisherman.name
