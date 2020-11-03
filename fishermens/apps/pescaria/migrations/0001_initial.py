# Generated by Django 3.1.2 on 2020-11-01 04:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fishing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fisherman_name', models.CharField(max_length=60, verbose_name='Nome do capitão')),
                ('immediate', models.CharField(max_length=60, verbose_name='Imediato')),
                ('pilot', models.CharField(max_length=60, verbose_name='Piloto')),
                ('friend', models.CharField(blank=True, max_length=60, null=True, verbose_name='Amigo')),
                ('fishing_day', models.DateField(verbose_name='Data da pesca')),
                ('fishing_hour', models.TimeField(verbose_name='Horário da pesca')),
                ('localization', models.CharField(max_length=100, verbose_name='Local da pesca')),
            ],
            options={
                'verbose_name': 'Fishing',
                'verbose_name_plural': 'Fisheries',
                'ordering': ['fishing_day'],
            },
        ),
    ]
