# Generated by Django 4.0 on 2022-03-30 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0096_tarifagre_facture_certagr'),
    ]

    operations = [
        migrations.AddField(
            model_name='facture_certagr',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
