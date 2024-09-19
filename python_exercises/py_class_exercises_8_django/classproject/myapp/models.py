from django.db import models

class Superhero(models.Model):
    HERO_MEDIUM_CHOICES = [
        ('movies', 'Movies'),
        ('comics', 'Comics'),
        ('videogames', 'Video Games'),
        ('tv', 'TV Shows'),
    ]

    heroname = models.CharField(max_length=100)
    realname = models.CharField(max_length=100)
    medium = models.CharField(max_length=20, choices=HERO_MEDIUM_CHOICES)

    def __str__(self):
        return self.heroname

class Creatures(models.Model):
    ORIGIN_CHOICES = [
        ('mythology', 'Mythology'),
        ('books', 'Books'),
        ('comics', 'Comics'),
        ('videogames', 'Video Games'),
        ('tv', 'TV Shows'),
        ('movies', 'Movies'),
    ]

    creaturename = models.CharField(max_length=100)
    origin = models.CharField(max_length=20, choices=ORIGIN_CHOICES)
    originname = models.CharField(max_length=100)

    def __str__(self):
        return self.creaturename
