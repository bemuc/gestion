# Generated by Django 4.0.2 on 2022-02-26 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0016_certificatagrement'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatagrement',
            name='date_created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]
