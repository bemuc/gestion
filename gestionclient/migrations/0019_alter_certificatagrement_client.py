# Generated by Django 4.0.2 on 2022-02-26 17:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0018_certificatagrement_expiration_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificatagrement',
            name='client',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, to='gestionclient.client'),
        ),
    ]