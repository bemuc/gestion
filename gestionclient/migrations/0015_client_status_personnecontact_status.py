# Generated by Django 4.0.2 on 2022-02-26 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0014_personnecontact'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='status',
            field=models.CharField(default='actif', max_length=200),
        ),
        migrations.AddField(
            model_name='personnecontact',
            name='status',
            field=models.CharField(default='actif', max_length=200),
        ),
    ]