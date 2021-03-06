# Generated by Django 3.1.2 on 2020-11-01 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0001_initial'),
        ('pescaria', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fishing',
            name='fisherman_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Capitão', to='usuario.user'),
        ),
        migrations.AlterField(
            model_name='fishing',
            name='friend',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Amigo', to='usuario.user'),
        ),
        migrations.AlterField(
            model_name='fishing',
            name='immediate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Imediato', to='usuario.user'),
        ),
        migrations.AlterField(
            model_name='fishing',
            name='pilot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Piloto', to='usuario.user'),
        ),
    ]
