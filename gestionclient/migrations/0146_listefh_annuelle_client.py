# Generated by Django 4.0 on 2022-04-21 07:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0145_listefh_annuelle_facture_fh_annuelle_faisceaux'),
    ]

    operations = [
        migrations.AddField(
            model_name='listefh_annuelle',
            name='client',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='gestionclient.client'),
        ),
    ]