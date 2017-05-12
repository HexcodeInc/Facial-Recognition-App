from __future__ import unicode_literals

from django.db import models

# Create your models here.
class news(models.Model):
	news_id = models.IntegerField(primary_key=True)

class game_Article(models.Model):
	id = models.OneToOneField(news,on_delete=models.CASCADE,primary_key=True)
	news_header = models.CharField(max_length=20)
	news_brief = models.CharField(max_length=50)
	news_link = models.CharField(max_length=40)
	def __str__(self):
		return self.news_header

class politics_Article(models.Model):
	id = models.OneToOneField(news,on_delete=models.CASCADE,primary_key=True)
	news_header = models.CharField(max_length=20)
	news_brief = models.CharField(max_length=50)
	news_link = models.CharField(max_length=40)
	def __str__(self):
		return self.news_header