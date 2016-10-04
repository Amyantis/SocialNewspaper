# Register your models here.
from django.contrib import admin

from ArticleManagement.models import Article, ArticleSharing, ArticleAuthor, Author, ArticleImage, ArticleKeyword, \
    ArticleTag, ArticleMeta

admin.site.register(Article)
admin.site.register(ArticleMeta)
admin.site.register(ArticleTag)
admin.site.register(ArticleKeyword)
admin.site.register(ArticleImage)
admin.site.register(Author)
admin.site.register(ArticleAuthor)
admin.site.register(ArticleSharing)
