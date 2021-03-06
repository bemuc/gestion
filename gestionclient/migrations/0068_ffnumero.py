# Generated by Django 4.0 on 2022-03-22 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0067_delete_ffnumero'),
    ]

    operations = [
        migrations.CreateModel(
            name='FFNumero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_pq', models.IntegerField(default=0, null=True)),
                ('q_ordinaire', models.IntegerField(default=0, null=True)),
                ('q_ussd', models.IntegerField(default=0, null=True)),
                ('q_mnemonique', models.IntegerField(default=0, null=True)),
                ('q_mnc', models.IntegerField(default=0, null=True)),
                ('q_nspc', models.IntegerField(default=0, null=True)),
                ('q_ispc', models.IntegerField(default=0, null=True)),
                ('q_cpti', models.IntegerField(default=0, null=True)),
                ('autorisation_arct', models.BooleanField(default=False)),
                ('nature', models.CharField(choices=[('Nouveau Client', 'Nouveau Client'), ('Renouvellement Client', 'Renouvellement Client')], max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionclient.client')),
            ],
        ),
    ]
