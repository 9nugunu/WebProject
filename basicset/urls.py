"""basicset URL Configuration

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
import func.views
import excurri.views
import DSUM.views
import competition.views
import tutoring.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', func.views.main, name='main'),
    path('excurri/', excurri.views.excurri, name='excurri'),
    path('dsum/', DSUM.views.dsum, name='dsum'),
    path('competition/', competition.views.competition, name='competition'),
    path('tutoring/', tutoring.views.tutoring, name='tutoring'),

]
