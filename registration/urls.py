from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

from .views import UpdateProfileView, ProfileView, UpdateLoginView, CreateProfileView, PasswordView, SuccessView


app_name = 'profiles'

urlpatterns = [
    url(r'create_profile/$', login_required(CreateProfileView.as_view()), name='create_profile'),
    url(r'update/(?P<pk>\d+)/$', login_required(UpdateProfileView.as_view()), name='update'),
    url(r'', login_required(ProfileView.as_view()), name='profile_home'),
    url(r'password_change/(?P<pk>\d+)/$', login_required(PasswordView.as_view()), name='password_change'),
    url(r'login_details/(?P<pk>\d+)/$', login_required(UpdateLoginView.as_view()), name='login_details'),
    url(r'profile_update/$', login_required(SuccessView.as_view()), name='profile_update'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
