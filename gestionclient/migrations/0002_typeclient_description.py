# Generated by Django 4.0 on 2022-02-17 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='typeclient',
            name='description',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
