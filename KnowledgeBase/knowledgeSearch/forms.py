from django import forms

class NewQuestion(forms.Form):
    question = forms.CharField(label = "Question", max_length=200)
    answer = forms.CharField(label = "Answer", max_length=500)

class Search(forms.Form):
    keywords = forms.CharField(label = "searchBox", max_length=50)

class Notify(forms.Form):
    note = forms.CharField(label = "write message", max_length=50)
