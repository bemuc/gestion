# Generated by Django 4.0 on 2022-03-24 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0087_facture_ffnumero_q_pq'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture_ffnumero',
            name='fsva',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facture_ffnumero',
            name='q_cpti',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facture_ffnumero',
            name='q_ispc',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facture_ffnumero',
            name='q_mnc',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facture_ffnumero',
            name='q_mnemonique',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facture_ffnumero',
            name='q_nspc',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facture_ffnumero',
            name='q_ordinaire',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='facture_ffnumero',
            name='q_ussd',
            field=models.FloatField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_pq',
            field=models.FloatField(max_length=200, null=True),
        ),
    ]
