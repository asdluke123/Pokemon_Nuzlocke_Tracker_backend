# Generated by Django 4.1 on 2022-09-07 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pnrDB', '0016_alter_run_badges_alter_run_deaths'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.EmailField(default='1@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='1', max_length=20),
        ),
    ]
