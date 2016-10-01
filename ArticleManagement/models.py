from django.db import models


class Article(models.Model):
    url = models.URLField(null=False, unique=True)
    title = models.CharField(null=False, max_length=30)
    authors = models.CharField(null=True, max_length=30)
    summary = models.CharField(null=True, max_length=300)
    text = models.CharField(null=False, max_length=5000)
    # top_img = models.CharField()
    # keywords
    # meta_data
    # meta_description
    # meta_favicon
    # meta_img
    # meta_keywords
    # meta_language
