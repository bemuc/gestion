# Generated by Django 4.0 on 2022-03-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0091_remove_ff_numero_datefin'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture_ffnumero',
            name='total_bif',
            field=models.FloatField(max_length=200, null=True),
        ),
    ]