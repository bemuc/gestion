# Generated by Django 4.0 on 2022-04-07 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0120_remove_taux_updated_alter_taux_dateatri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taux',
            name='dateAtri',
            field=models.DateTimeField(null=True),
        ),
    ]
