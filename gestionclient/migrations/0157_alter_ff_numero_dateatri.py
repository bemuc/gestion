# Generated by Django 4.0.2 on 2022-06-20 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0156_certagr_dejarenou_alter_ab_dateatri_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ff_numero',
            name='dateAtri',
            field=models.DateField(null=True),
        ),
    ]