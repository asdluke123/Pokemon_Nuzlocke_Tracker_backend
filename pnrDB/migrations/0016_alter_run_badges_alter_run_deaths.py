# Generated by Django 4.1 on 2022-09-04 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnrDB', '0015_pokemonmove_level'),
    ]

    operations = [
        migrations.AlterField(
            model_name='run',
            name='badges',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='run',
            name='deaths',
            field=models.IntegerField(default=0),
        ),
    ]
