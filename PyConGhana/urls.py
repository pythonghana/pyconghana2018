"""PyConGhana URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404, handler500, handler403, handler400
from jet.dashboard.dashboard_modules import google_analytics_views


urlpatterns = [
    path('', include('home.urls', namespace='home')),
    path('about/', include('about.urls', namespace='about')),
    #path('accounts/', include('registration.backends.default.urls')),
    path('accounts/', include('registration.backends.simple.urls')),
    path('profile/', include('registration.urls', namespace='profiles')),
    # path('accounts/', include('accounts.urls', namespace='accounts')),
    path('avatar/', include('avatar.urls')),
    path('coc/', include('coc.urls', namespace='coc')),
    # path('contact/', include('contact.urls', namespace='contact')),
    path('schedule/', include('schedule.urls', namespace='schedule')),
    path('support_us/', include('support_us.urls', namespace='support_us')),
    path('sponsors/', include('sponsors.urls', namespace='sponsors')),
    path('prospectus/', include('sponsors.urls', namespace='Prospectus')),
    path('talks/', include('talks.urls', namespace='talks')),
    path('privacypolicy/', include('privacypolicy.urls', namespace='privacypolicy')),
    path('newsletter/', include('newsletter.urls')),
    path('tinymce/', include('tinymce.urls')),
    path('jet/', include('jet.urls', 'jet')),  # Django JET URLS
    path('jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('faq/', include('faq.urls', namespace='faqs')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


# Adds ``STATIC_URL`` to the context of error pages, so that error
# pages can use JS, CSS and images.

handler400 = 'home.views.bad_request'
handler403 = 'home.views.permission_denied'
handler404 = 'home.views.page_not_found'
handler500 = 'home.views.server_error'