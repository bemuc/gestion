# Generated by Django 4.0 on 2022-02-19 09:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0002_typeclient_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('descrption', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CatService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Constructeur',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('adresse', models.CharField(max_length=200)),
                ('téléphone', models.CharField(max_length=200)),
                ('fax', models.CharField(max_length=200, null=True)),
                ('email', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Equipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('désignation', models.CharField(max_length=200)),
                ('marque', models.CharField(max_length=200)),
                ('modèle', models.CharField(max_length=200)),
                ('pays_origine', models.CharField(max_length=200)),
                ('constructeur', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionclient.constructeur')),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typeService', models.CharField(max_length=200)),
                ('nom', models.CharField(max_length=200)),
                ('categorie', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionclient.catservice')),
            ],
        ),
        migrations.CreateModel(
            name='TypeEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=200, null=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionclient.categoryequipement')),
            ],
        ),
        migrations.CreateModel(
            name='Tarifs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200)),
                ('montant', models.CharField(max_length=200)),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionclient.service')),
            ],
        ),
        migrations.CreateModel(
            name='HomologationEquipement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionclient.client')),
                ('equipement', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionclient.equipement')),
            ],
        ),
        migrations.AddField(
            model_name='equipement',
            name='type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gestionclient.typeequipement'),
        ),
    ]
