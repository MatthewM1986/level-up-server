from django.db import models


class Event(models.Model):
    date = models.DateField()
    time = models.TimeField()
    game = models.ForeignKey("Game", on_delete=models.CASCADE)
    location = models.CharField(max_length=55)
    organizer = models.ForeignKey("Gamer", on_delete=models.CASCADE)
    description = models.CharField(max_length=255)
