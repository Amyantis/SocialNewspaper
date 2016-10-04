import newspaper
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.db import transaction
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from ArticleManagement.forms import ArticleSharingForm
from ArticleManagement.models import Article, ArticleSharing, ArticleImage, Author, ArticleAuthor, ArticleKeyword, \
    ArticleTag, ArticleMeta


def share_article(request):
    return render(request, 'form_share_article.html', {'form': ArticleSharingForm})


@login_required
def insert_article(request):
    template = loader.get_template('article.html')

    if request.method == 'POST':
        form = ArticleSharingForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']

            article = newspaper.Article(url)

            article.download()

            article.parse()

            try:
                # transaction

                try:
                    article_obj = Article.objects.get(url=url)
                except ObjectDoesNotExist:
                    article_obj = \
                        Article(
                            url=url,
                            title=article.title,
                            summary=article.summary,
                            text=article.text,
                            top_img=article.top_image
                        )
                    article_obj.save()

                    for image in article.images:
                        ArticleImage(
                            article=article_obj,
                            img_adress=image
                        ).save()
                    for author in article.authors:
                        author = Author(
                            author=author
                        )
                        author.save()
                        ArticleAuthor(
                            article=article_obj,
                            author=author
                        ).save()
                    for keyword in article.keywords:
                        if keyword == '':
                            continue
                        ArticleKeyword(
                            article=article_obj,
                            keyword=keyword
                        ).save()
                    for tag in article.tags:
                        ArticleTag(
                            article=article_obj,
                            keyword=tag
                        ).save()
                    ArticleMeta(
                        article=article_obj,
                        meta_data=article.meta_data,
                        meta_description=article.meta_description,
                        meta_favicon=article.meta_favicon,
                        meta_img=article.meta_img,
                        meta_keywords=article.meta_keywords,
                        meta_language=article.meta_lang
                    ).save()

                article_sharing = ArticleSharing(
                    article=article_obj,
                    user=request.user
                )

                article_sharing.save()

            except IntegrityError:
                transaction.rollback()

            context = {
                'articles': [article_obj.__dict__]
            }

            return HttpResponse(template.render(context, request))


def print_articles_without_count(request):
    template = loader.get_template('article.html')
    articles = Article.objects.all()

    context = {
        'articles': [article.__dict__ for article in articles]
    }

    return HttpResponse(template.render(context, request))


def print_articles(request):
    template = loader.get_template('article.html')

    # TODO: replace the queries above with row SQL to optimize

    articles = Article.objects.all()

    context = {
        'articles': _zip_sharings_to_article(articles)
    }

    return HttpResponse(template.render(context, request))


def _zip_sharings_to_article(articles):
    for article in articles:
        sharings = len(ArticleSharing.objects.filter(article=article))
        yield dict(article.__dict__, **{'sharings': sharings})
