# Generated by Django 4.0 on 2022-03-22 17:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0062_alter_chiffreaffaire_options_alter_client_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='FFNumero',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('q_pq', models.IntegerField(null=True)),
                ('q_ordinaire', models.IntegerField(null=True)),
                ('q_ussd', models.IntegerField(null=True)),
                ('q_mnemonique', models.IntegerField(null=True)),
                ('q_mnc', models.IntegerField(null=True)),
                ('q_nspc', models.IntegerField(null=True)),
                ('q_ispc', models.IntegerField(null=True)),
                ('q_cpti', models.IntegerField(null=True)),
                ('nature', models.CharField(choices=[('Nouveau Client', 'Nouveau Client'), ('Renouvellement Client', 'Renouvellement Client')], max_length=200, null=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='gestionclient.client')),
            ],
        ),
    ]
