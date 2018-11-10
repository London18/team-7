from django.shortcuts import render
from django.http import HttpResponse
from knowledgeSearch.models import Article, Contact, Ticket
from datetime import datetime, timedelta
from .forms import NewQuestion, Search, Notify
from random import randint
from django.views import View

class MainView(View):
    template_name = 'knowledgeSearch/index.html'


    def get(self, request):
        hour = datetime.now() - timedelta(seconds = 15)
        Ticket.objects.filter(submitTime__lte = hour).delete()

        article_list = Article.objects.all()
        contact_list = Contact.objects.all()
        ticket_list = Ticket.objects.all()

        form = NewQuestion()
        search = Search()
        makenotify = Notify()
        args = {
           "article_list" : article_list,
           "contact_list" : contact_list,
           "notification_list" : ticket_list,
            "form" : form,
            "search": search,
            "makenotify": makenotify
        }
        return render(request, self.template_name, args)
    
    def post(self, request):
        hour = datetime.now() - timedelta(seconds = 15)
        Ticket.objects.filter(submitTime__lte = hour).delete()

        form = NewQuestion(request.POST)
        search = Search(request.POST)
        makenotify = Notify(request.POST)

        
        article_list = Article.objects.all()
        contact_list = Contact.objects.all()
        ticket_list = Ticket.objects.all()

        args = {
            "article_list" : article_list,
            "contact_list" : contact_list,
            "notification_list" : ticket_list,
            "form" : form,
            "search": search,
            "makenotify": makenotify
        }
        if form.is_valid():
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            a = Article(title = question, body = answer)
            args['article_list']= Article.objects.all()
            a.save()
        if search.is_valid():
            searched = search.cleaned_data['keywords']
            args['article_list']= Article.objects.filter(title__contains=str(searched) )
            return render(request, self.template_name, args)
        if makenotify.is_valid():
            notificiation = makenotify.cleaned_data['note']
            rand = 0
            while True:
                rand = randint(1,10000)
                if Ticket.objects.filter(number = rand).count() == 0:
                    break
            p = Ticket(number = rand, notes = notificiation)
            p.save()

        return render(request, self.template_name,args)

