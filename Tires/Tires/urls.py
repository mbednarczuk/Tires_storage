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
from tires_shop import views as views
from tires_shop import views as core_views

from tires_shop.views import (TiresView, Login, Logout, TiresListView, TireSearchView, NewTireView, TireDetailView,
                              ChangePasswordView, OrderView, AllOrders, OrderDelete, OwnerView, ClientView,
                              BrandsDescribeDetailView,
                              NewBrandView)

urlpatterns = [
                  url(r'^admin/', admin.site.urls),
                  url(r'^tires$', TiresView.as_view(), name="start"),
                  url(r'^login$', Login.as_view(), name='login'),
                  url(r'^logout$', Logout.as_view(), name='logout'),
                  url(r'^all_tires$', TiresListView.as_view(), name='list'),
                  url(r'^tire_search', TireSearchView.as_view(), name='search_tire'),
                  url(r'^add_tire$', NewTireView.as_view(), name="new"),
                  url(r'^signup/$', core_views.signup, name='signup'),
                  url(r'^contact/$', views.contact, name='contact'),
                  url(r'^order$', OrderView.as_view(), name='order'),
                  url(r'^all_orders$', AllOrders.as_view(), name='all_orders'),
                  url(r'^owner$', OwnerView.as_view(), name="owner_start"),
                  url(r'^all_client$', ClientView.as_view(), name="client_start"),
                  url(r'^add_brand$', NewBrandView.as_view(), name="add_brand"),

                  url(r'^delete_order/(?P<pk>(\d)+)', OrderDelete.as_view(), name='order_delete'),
                  url(r'^edit_tire/(?P<pk>\d+)$', views.TireUpdate.as_view(), name='tire_edit'),
                  url(r'^delete_tire/(?P<pk>\d+)$', views.TireDelete.as_view(), name='tire_delete'),
                  url(r'^tire_detail/(?P<pk>(\d)+)', TireDetailView.as_view(), name='tire_detail'),
                  url(r'^reset_password/(?P<user_id>(\d)+)', ChangePasswordView.as_view(), name='change_password'),
                  url(r'^brand_detail/(?P<pk>(\d)+)', BrandsDescribeDetailView.as_view(), name='brand_detail'),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
