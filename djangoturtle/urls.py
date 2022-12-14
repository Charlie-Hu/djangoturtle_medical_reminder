"""djangoturtle URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app01 import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.log_in),
    path('register/', views.register),
    path('main/', views.main),
    path('jump/', views.jump),
    path('plan/', views.plan),
    path('logout/', views.log_out),
    # path('delete/', views.plan_delete, name='delete'),
    path('hardware/', views.Hardware_View.as_view()),
    path('send_email/', views.send_email)
]
