# Generated by Django 4.0 on 2022-02-21 08:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0006_remove_materiel_quantite'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reseauxnoncommercial',
            name='rubrique',
        ),
        migrations.AddField(
            model_name='reseauxnoncommercial',
            name='rubrique',
            field=models.ManyToManyField(to='gestionclient.RubriqueFacturation'),
        ),
    ]
