# Generated by Django 4.0.2 on 2022-02-26 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0017_certificatagrement_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificatagrement',
            name='expiration_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='certificatagrement',
            name='expired',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='certificatagrement',
            name='status',
            field=models.CharField(default='actif', max_length=200),
        ),
    ]
