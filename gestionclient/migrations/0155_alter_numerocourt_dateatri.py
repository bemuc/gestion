# Generated by Django 4.0 on 2022-04-25 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0154_alter_constructeur_date_creation_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='numerocourt',
            name='dateAtri',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]