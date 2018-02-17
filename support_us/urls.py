from django.urls import path
from . import views

app_name = 'support_us'
urlpatterns = [
    path('', views.support_us,name='support_us')
]