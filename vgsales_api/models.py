from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=120)
    platform = models.CharField(max_length=20)
    year = models.IntegerField()
    genre = models.CharField(max_length=50)
    publisher = models.CharField(max_length=120)
    na_sales = models.FloatField()
    eu_sales = models.FloatField()
    jp_sales = models.FloatField()
    other_sales = models.FloatField()
    global_sales = models.FloatField()

    def __str__(self) -> str:
        return self.name

