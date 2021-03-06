# Generated by Django 4.0 on 2022-03-24 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0083_rename_fs_agreequipe_tarifffnumero_etudedossier_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarifFSVANumero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('etudeDossier', models.FloatField(max_length=200, null=True)),
                ('agrementEquip', models.FloatField(max_length=200, null=True)),
                ('redevanceAnn', models.FloatField(max_length=200, null=True)),
                ('autorisationARCT', models.FloatField(max_length=200, null=True)),
                ('etat', models.CharField(default='actif', max_length=200, null=True)),
                ('dateAtri', models.DateField(auto_now=True, null=True)),
            ],
        ),
    ]
