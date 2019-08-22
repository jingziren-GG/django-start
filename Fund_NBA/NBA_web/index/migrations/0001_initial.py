# Generated by Django 2.0.8 on 2019-02-20 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NBAData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.IntegerField(verbose_name='排名')),
                ('ballgame', models.CharField(max_length=50, verbose_name='球队')),
                ('win', models.IntegerField(verbose_name='胜场')),
                ('transport', models.IntegerField(verbose_name='败场')),
                ('winrate', models.CharField(max_length=50, verbose_name='胜率')),
                ('logopath', models.ImageField(upload_to='images', verbose_name='球队logo')),
                ('area', models.CharField(max_length=50, verbose_name='区域')),
            ],
        ),
    ]