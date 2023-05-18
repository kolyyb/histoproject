from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=45)


class Card(models.Model):
    quest = models.TextField()
    sugg_a = models.CharField(max_length=150)
    sugg_b = models.CharField(max_length=150)
    sugg_c = models.CharField(max_length=150)
    sugg_d = models.CharField(max_length=150)
    res = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)



