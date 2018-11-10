from django.shortcuts import render
from django.http import HttpResponse
from knowledgeSearch.models import Article
# Create your views here.


def index(request):

    #a = Article(title = "this is just a test", body = "this is the body of the thing")
    #a.save()
    
    article_list = Article.objects.all()

    args = {"article_list" : article_list}

    return render(request, 'knowledgeSearch/index.html', args)