from django.contrib import admin
from .models import game_Article,politics_Article,news
# Register your models here.
admin.site.register(game_Article)
admin.site.register(politics_Article)
admin.site.register(news)