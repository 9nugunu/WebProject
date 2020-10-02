"""
basicset URL Configuration
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
import main_app.views
import DSUM_app.views
import tutoring_app.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_app.views.main, name='main'),
    path('excurri/', main_app.views.excurri, name='excurri'),
    path('dsum/', DSUM_app.views.dsum, name='dsum'),
    path('contest/', main_app.views.contest, name='contest'),
    path('tutoring/', tutoring_app.views.tutoring, name='tutoring'),
]
