# Generated by Django 4.0.3 on 2022-04-16 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0134_remove_tariffh_repere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tariffh',
            name='nature',
            field=models.IntegerField(choices=[(23, '>23'), (13, '>13'), (3, '>3'), (0, '<3')], max_length=200, null=True),
        ),
    ]
