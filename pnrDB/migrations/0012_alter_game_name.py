# Generated by Django 4.1 on 2022-09-02 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnrDB', '0011_boxpokemon'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(choices=[('Vintage White', 'Vintage White')], default='Vintage White', max_length=30),
        ),
    ]
