from django.urls import path
from .views import MainView


urlpatterns = [
    path('index/', MainView.as_view(), name = 'main-view'),
    #path('index', views.index),
   # path('ticket', views.ticket),
]