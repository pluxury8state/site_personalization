from django.db import models


class Player(models.Model):

    def __str__(self):
        return f'player - {self.id}'


class Game(models.Model):
    player_game_info = models.ManyToManyField(Player, through='PlayerGameInfo', related_name='GamePlayerInfo')
    hidden_number = models.IntegerField(null=True)
    player_try_count = models.IntegerField(null=True, default=0)
    guess_count = models.IntegerField(null=True, default=None)
    exists = models.BooleanField(default=True)
    iniciator = models.IntegerField(null=True)

    def __str__(self):
        return f'game {self.id}'


class PlayerGameInfo(models.Model):
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

