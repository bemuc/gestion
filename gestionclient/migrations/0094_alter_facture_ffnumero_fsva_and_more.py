# Generated by Django 4.0 on 2022-03-26 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0093_alter_facture_ffnumero_fsva_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='fsva',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_cpti',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_ispc',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_mnc',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_mnemonique',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_nspc',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_ordinaire',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_pq',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='q_ussd',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='total',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='facture_ffnumero',
            name='total_bif',
            field=models.IntegerField(null=True),
        ),
    ]
