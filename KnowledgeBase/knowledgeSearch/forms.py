from django import forms

class NewQuestion(forms.Form):
    firstName = forms.CharField(label = "First Name", max_length=30)
    lastName = forms.CharField(label = "Last Name", max_length=30)
    question = forms.CharField(label = "Question", max_length=200)
    answer = forms.CharField(label = "Answer", max_length=500)

class Search(forms.Form):
    keywords = forms.CharField(label = "searchBox", max_length=50)