from django.shortcuts import render
from django.http import HttpResponse
from knowledgeSearch.models import Article
# Create your views here.


def index(request):
    article_list = Article.objects.all()

    args = {"article_list" : article_list}

    return render(request, 'knowledgeSearch/index.html', args)

def add(request):
    pass