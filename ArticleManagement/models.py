from django.contrib.auth.models import User
from django.db import models


# class ArticleManager(models.Manager):
#     def get_queryset(self):
#         articles = super(ArticleManager, self).get_queryset()
#
#         return

class Article(models.Model):
    url = models.URLField(null=False, unique=True)
    title = models.CharField(null=False, max_length=30)
    summary = models.CharField(null=True, max_length=300)
    text = models.CharField(null=False, max_length=5000)

    top_img = models.CharField(null=False, max_length=300)

    def authors(self):
        return ArticleAuthor.objects.filter(article=self).only("author")



class ArticleMeta(models.Model):
    article = models.OneToOneField(Article)
    meta_data = models.CharField(null=True, max_length=150)
    meta_description = models.CharField(null=True, max_length=150)
    meta_favicon = models.CharField(null=True, max_length=300)
    meta_img = models.CharField(null=True, max_length=300)
    meta_keywords = models.CharField(null=True, max_length=300)
    meta_language = models.CharField(null=True, max_length=30)


class ArticleTag(models.Model):
    article = models.ForeignKey(Article)
    tag = models.CharField(null=False, max_length=30)


class ArticleKeyword(models.Model):
    article = models.ForeignKey(Article)
    keyword = models.CharField(null=False, max_length=30)


class ArticleImage(models.Model):
    article = models.ForeignKey(Article)
    img_adress = models.CharField(null=False, max_length=300)


class Author(models.Model):
    author = models.CharField(null=False, max_length=30, unique=True)


class ArticleAuthor(models.Model):
    article = models.ForeignKey(Article)
    author = models.ForeignKey(Author)

    class Meta:
        unique_together = ('article', 'author')


class ArticleSharing(models.Model):
    sharing_date = models.DateTimeField(auto_now=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
