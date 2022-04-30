from django.db import models


class Game(models.Model):
    name = models.CharField(max_length=200)
    platform = models.CharField(max_length=20, blank=True, null=True)
    year = models.IntegerField(blank=True, null=True)
    genre = models.CharField(max_length=50, blank=True, null=True)
    publisher = models.CharField(max_length=200, blank=True, null=True)
    na_sales = models.FloatField(blank=True, null=True)
    eu_sales = models.FloatField(blank=True, null=True)
    jp_sales = models.FloatField(blank=True, null=True)
    other_sales = models.FloatField(blank=True, null=True)
    global_sales = models.FloatField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name

