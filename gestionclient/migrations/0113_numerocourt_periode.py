# Generated by Django 4.0 on 2022-04-04 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0112_tarifhom_facturehom'),
    ]

    operations = [
        migrations.AddField(
            model_name='numerocourt',
            name='periode',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
