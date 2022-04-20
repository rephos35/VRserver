"""Project_rest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include
from VRserver.views import status_view
from display.views import last_data_view, all_data_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('status/', status_view, name='status'),
    path('last_data/', last_data_view, name='last_data'),
    path('all_data/',all_data_view, name='all_data')
]
