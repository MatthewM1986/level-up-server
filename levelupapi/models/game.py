from django.db import models


class Game(models.Model):
    title = models.CharField(max_length=55)
    game_type = models.ForeignKey("GameType", on_delete=models.CASCADE)
    number_of_players = models.IntegerField()
    gamer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
