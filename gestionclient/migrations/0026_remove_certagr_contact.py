# Generated by Django 4.0 on 2022-03-02 18:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0025_alter_personnecontact_client'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='certagr',
            name='contact',
        ),
    ]
