# Generated by Django 4.0 on 2022-03-22 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0069_ffnumero_etat_ffnumero_facturer'),
    ]

    operations = [
        migrations.AddField(
            model_name='ffnumero',
            name='dateAtri',
            field=models.DateField(null=True),
        ),
    ]
