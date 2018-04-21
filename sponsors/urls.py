from django.urls import path
from . import views

app_name = 'sponsors'
urlpatterns = [
    path('', views.sponsors, name='sponsors'),
    path('apply', (views.apply), name='apply'),
    path('prospectus', views.sponsors, name='Prospectus')
]
