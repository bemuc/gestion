# Generated by Django 4.0 on 2022-03-23 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0071_ff_numero_delete_ffnumero'),
    ]

    operations = [
        migrations.AddField(
            model_name='ff_numero',
            name='FS_agreEquipe',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ff_numero',
            name='FS_autoARCT',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ff_numero',
            name='FS_etudeDossier',
            field=models.BooleanField(default=False),
        ),
    ]
