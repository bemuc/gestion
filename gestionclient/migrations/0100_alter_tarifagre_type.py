# Generated by Django 4.0 on 2022-03-30 09:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0099_tarifagre_tarif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarifagre',
            name='type',
            field=models.CharField(choices=[('VENDEUR', 'VENDEUR'), ('INSTALLATEUR', 'INSTALLATEUR'), ('DISTRIBUTEUR', 'DISTRIBUTEUR')], max_length=200, null=True),
        ),
    ]
