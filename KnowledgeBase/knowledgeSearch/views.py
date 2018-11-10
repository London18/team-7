from django.shortcuts import render
from django.http import HttpResponse
from knowledgeSearch.models import Article, Contact, Ticket
from datetime import datetime, timedelta
from .forms import NewQuestion, Search
from random import randint
# Create your views here.



from django.views import View

class MainView(View):
    template_name = 'knowledgeSearch/index.html'
    article_list = Article.objects.all()
    contact_list = Contact.objects.all()
   
    def get(self, request):
        form = NewQuestion()
        search = Search()
        args = {
           "article_list" : self.article_list,
           "contact_list" : self.contact_list,
            "form" : form,
            "search": search
        }
        return render(request, self.template_name, args)
    
    def post(self, request):
        form = NewQuestion(request.POST)
        search = Search(request.POST)
        a = None
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            question = form.cleaned_data['question']
            answer = form.cleaned_data['answer']
            a = Article(title = question, body = answer)
        if search.is_valid():
            searched = search.cleaned_data['keywords']
            print(searched)
        args = {
            "article_list" : self.article_list,
            "contact_list" : self.contact_list,
            "form" : form,
            "search": search
        }

        if a != None:
            print("Added")
            a.save()

        return render(request, self.template_name,args)

"""
def ticket(request):
    #delete all entries older than 4 hours
    Ticket.objects.filter(submitTime__gte = datetime.now()-timedelta(minutes = 1)).delete()
    index = 0
    while True:
        index = randint(1, 10000)
        if Ticket.objects.filter(number = index).exists():
            pass
        else:
            break
    message = "This is a temporary thing which is going to be changed when the other stuff works"
    print(Ticket.objects.all())
    #p = Ticket(number = index, notes = message)
    #p.save()
    return HttpResponse("<h1> your ticket has been added</h1>") 
    """