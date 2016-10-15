"""SocialNewspaper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from ArticleManagement import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^share_article/$', views.share_article, name="share_article"),
    url(r'^print_sharing/(?P<article_id>[0-9]+)$', views.print_sharing, name="print_sharing"),
    url(r'^insert_article/$', views.insert_article, name="insert_article"),
    url(r'^add_interesting/(?P<article_id>[0-9]+)$', views.add_interesting, name="add_interesting"),
    url(r'^print_articles/$', views.print_articles, name="print_articles"),
    url(r'^$', views.print_articles)
]
