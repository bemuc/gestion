# Generated by Django 4.0 on 2022-03-30 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0103_facture_certagr_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='facture_certagr',
            name='client',
        ),
    ]
