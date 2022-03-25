# Generated by Django 4.0 on 2022-03-23 17:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0074_numerocourt_ffnumero'),
    ]

    operations = [
        migrations.AddField(
            model_name='pq',
            name='ffnumero',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionclient.ff_numero'),
        ),
        migrations.AlterField(
            model_name='numerocourt',
            name='numero',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
