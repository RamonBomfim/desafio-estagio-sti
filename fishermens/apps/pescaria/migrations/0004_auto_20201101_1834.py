# Generated by Django 3.1.2 on 2020-11-01 21:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('pescaria', '0003_auto_20201101_1735'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishing',
            name='immediate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Imediato', to='usuario.user', verbose_name='Imediato'),
        ),
        migrations.AlterField(
            model_name='fishing',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Piloto', to='usuario.user', verbose_name='Piloto'),
        ),
    ]
