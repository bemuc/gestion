# Generated by Django 4.0 on 2022-03-24 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0085_ff_numero_efacturer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture_ffnumero',
            name='client',
        ),
        migrations.AddField(
            model_name='ff_numero',
            name='periode',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
