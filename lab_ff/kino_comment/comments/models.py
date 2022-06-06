from django.db import models


class Kino(models.Model):
    kino_name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=80)
    country = models.CharField(max_length=30)
    director = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.kino_name}  {self.description} {self.genre} {self.country} {self.director}"


class Price(models.Model):
    name = models.CharField(max_length=255)
    money = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "prices"

    def __str__(self):
        return self.name