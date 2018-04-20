from rest_framework import routers
from django.urls import include, path, re_path
from talks.views import TalkViewsSets
from django.conf.urls import url
from django.contrib.auth.decorators import login_required
from talks import views


app_name = 'talks'
router = routers.DefaultRouter()
router.register(r'talks', TalkViewsSets)

urlpatterns = [
    path('accepted_talks', views.AcceptedTalksView.as_view(), name='accepted_talks'),
    path('submit_talk', login_required(views.submit_talk), name='submit_talk'),
    re_path(r'^edit_talk/(?P<pk>\d+)', login_required(views.TalkView.as_view()), name='edit_talk'),
    path('talk_list', login_required(views.TalkList.as_view()), name='talk_list'),
    re_path(r'^talk_details/(?P<pk>\d+)', views.TalkDetailView.as_view(), name='talk_details'),
    path('submitted', login_required(views.SuccessView.as_view()), name='submitted'),
    path('uploads', views.home, name='home'),
    path('submit', views.submit, name='submit'),
    path('proposing_a_talk', views.proposing, name='proposing'),
    path('recording', views.recording, name='recording'),
    path('uploads_simple', views.simple_upload, name='simple_upload'),
    path('uploads_form', views.model_form_upload, name='model_form_upload'),
    ]

urlpatterns += router.urls

