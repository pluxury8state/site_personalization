# Generated by Django 2.2.10 on 2020-10-09 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hidden_number', models.IntegerField(null=True)),
                ('player_try_count', models.IntegerField(default=0, null=True)),
                ('guess_count', models.IntegerField(default=None, null=True)),
                ('exists', models.BooleanField(default=True)),
                ('iniciator', models.IntegerField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Player',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='PlayerGameInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Game')),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='game.Player')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='player_game_info',
            field=models.ManyToManyField(related_name='GamePlayerInfo', through='game.PlayerGameInfo', to='game.Player'),
        ),
    ]
