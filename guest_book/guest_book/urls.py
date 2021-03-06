"""guest_book URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path

from check_in.views import guest_list_view, guest_add_view, guest_data_update, guest_data_delete, guest_search

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', guest_list_view, name='guest-list'),
    path('add/', guest_add_view, name='guest-add'),
    path('guest/<int:pk>/update/', guest_data_update, name='guest-data-update'),
    path('guest/<int:pk>/delete/', guest_data_delete, name='guest-data-delete'),
    path('guest/', guest_search, name='guest-search'),
]
