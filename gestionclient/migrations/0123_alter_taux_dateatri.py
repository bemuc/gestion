# Generated by Django 4.0 on 2022-04-07 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0122_alter_taux_dateatri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taux',
            name='dateAtri',
            field=models.DateTimeField(null=True),
        ),
    ]