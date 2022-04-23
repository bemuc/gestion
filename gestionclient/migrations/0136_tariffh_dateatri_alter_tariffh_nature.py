# Generated by Django 4.0.3 on 2022-04-16 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0135_alter_tariffh_nature'),
    ]

    operations = [
        migrations.AddField(
            model_name='tariffh',
            name='dateAtri',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='tariffh',
            name='nature',
            field=models.IntegerField(choices=[(23, '>23'), (13, '>13'), (3, '>3'), (0, '<3')], null=True),
        ),
    ]
