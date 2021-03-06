# Generated by Django 4.0 on 2022-03-17 10:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0041_alter_certagr_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=200, null=True)),
                ('prix', models.FloatField(max_length=200, null=True)),
                ('status', models.CharField(choices=[('ACTIF', 'ACTIF'), ('NON ACTIF', 'NON ACTIF')], max_length=200, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='certagr',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionclient.category'),
        ),
    ]
