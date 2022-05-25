# Generated by Django 4.0.3 on 2022-04-16 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestionclient', '0128_alter_faisceauxhertzien_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='TarifFH',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('repere', models.IntegerField(null=True)),
                ('p_canal', models.FloatField(max_length=200, null=True)),
                ('p_mhz', models.FloatField(max_length=200, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='faisceauxhertzien',
            name='dateAtri',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]