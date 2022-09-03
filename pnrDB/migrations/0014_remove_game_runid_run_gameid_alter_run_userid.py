# Generated by Django 4.1 on 2022-09-02 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pnrDB', '0013_rename_pokemoid_boxpokemon_pokemonid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='runId',
        ),
        migrations.AddField(
            model_name='run',
            name='gameId',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='runs', to='pnrDB.game'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='run',
            name='userId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='game', to='pnrDB.user'),
        ),
    ]