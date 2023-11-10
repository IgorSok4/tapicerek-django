from django.contrib import admin
from django.urls import path, include

from wagtail.admin import urls as wagtailadmin_urls

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path("admin/", include(wagtailadmin_urls)),
    path('', include('main.urls')),
]
