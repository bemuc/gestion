# Generated by Django 4.0 on 2022-03-30 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0100_alter_tarifagre_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='certagr',
            name='facturer',
            field=models.CharField(default='non', max_length=200, null=True),
        ),
    ]