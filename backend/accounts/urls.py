# Django Only
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from accounts.views import *

urlpatterns = [
    path('login/', login_view, name="login_page"),
    path('check/', check, name="check"),
    path('verify/', verify, name="verify"),
    path('verified/', verified, name="verified"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)