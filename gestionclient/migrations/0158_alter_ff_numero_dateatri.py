# Generated by Django 4.0.2 on 2022-06-20 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0157_alter_ff_numero_dateatri'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ff_numero',
            name='dateAtri',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
