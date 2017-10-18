"""Tires URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from tires_shop.views import TiresView, Login, Logout, TiresListView, TireSearchView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tires$', TiresView.as_view(), name="start"),
    url(r'^login$', Login.as_view(), name='login'),
    url(r'^logout$', Logout.as_view(), name='logout'),
    url(r'^tires_list$', TiresListView.as_view(), name="list"),
    url(r'^tire_search', TireSearchView.as_view(), name='szukaj'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
