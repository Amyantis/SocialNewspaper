# Register your models here.
from django.contrib import admin

from ArticleManagement.models import Article, ArticleSharing

admin.site.register(Article)
admin.site.register(ArticleSharing)
