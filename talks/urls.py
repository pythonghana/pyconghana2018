from django.urls import path
from . import views

app_name = 'talks'
urlpatterns = [
    path('', views.talks,name='talks')
]