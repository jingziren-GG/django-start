# -*- coding:utf-8 -*-
from django.db import models

# Create your models here.


class NBAData(models.Model):
    ranking = models.IntegerField(verbose_name='排名')
    ballgame = models.CharField(max_length=50,verbose_name='球队')
    win = models.IntegerField(verbose_name='胜场')
    transport = models.IntegerField(verbose_name='败场')
    winrate = models.CharField(max_length=50,verbose_name='胜率')
    logopath = models.ImageField(null=False, upload_to="images", verbose_name="球队logo")
    area = models.CharField(max_length=50,verbose_name='区域')

    def __str__(self):
        return self.ballgame