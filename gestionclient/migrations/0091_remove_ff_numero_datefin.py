# Generated by Django 4.0 on 2022-03-25 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0090_alter_ff_numero_datefin'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ff_numero',
            name='dateFin',
        ),
    ]
