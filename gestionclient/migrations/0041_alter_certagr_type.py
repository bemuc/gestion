# Generated by Django 4.0 on 2022-03-16 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0040_certagr_pourfacturation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certagr',
            name='type',
            field=models.CharField(choices=[('VENDEUR', 'VENDEUR'), ('INSTALLATEUR', 'INSTALLATEUR'), ('DISTRIBUTEUR', 'DISTRIBUTEUR')], max_length=200, null=True),
        ),
    ]
