from django.db import models


class Kino(models.Model):
    kino_name = models.CharField(max_length=30)
    description = models.CharField(max_length=1000)
    genre = models.CharField(max_length=80)
    country = models.CharField(max_length=30)
    director = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.kino_name}"


class Price(models.Model):
    name = models.CharField(max_length=255)
    money = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "prices"

    def __str__(self):
        return self.name


class Comment(models.Model):
    kino = models.ForeignKey(Kino, on_delete=models.CASCADE)
    author = models.CharField('автор', max_length=100)
    text = models.TextField('текст комментария')


class Add(models.Model):
    name = models.CharField(max_length=30)
    kino = models.TextField()

    def __str__(self):
        return f"{self.name} предложил посмотреть {self.kino}"
