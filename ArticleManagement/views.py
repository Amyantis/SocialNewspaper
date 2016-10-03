import newspaper
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

from ArticleManagement.forms import ArticleSharingForm
from ArticleManagement.models import Article


def share_article(request):
    return render(request, 'form_share_article.html', {'form': ArticleSharingForm})


def insert_article(request):
    template = loader.get_template('article.html')

    if request.method == 'POST':
        form = ArticleSharingForm(request.POST)

        if form.is_valid():
            url = form.cleaned_data['url']

            article = newspaper.Article(url)

            article.download()

            article.parse()

            print(article.top_image)

            article_obj = \
                Article(
                    url=url,
                    title=article.title,
                    authors=article.authors,
                    summary=article.summary,
                    text=article.text
                )

            article_obj.save()

            context = {
                'articles': [article_obj.__dict__]
            }

            return HttpResponse(template.render(context, request))


def print_articles(request):
    template = loader.get_template('article.html')
    articles = Article.objects.all()

    context = {
        'articles': [article.__dict__ for article in articles]
    }

    return HttpResponse(template.render(context, request))
