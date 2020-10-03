from django.urls import path
from . import views

urlpatterns = [

    path('', views.main, name='main'),
    path('excurri/', views.excurri, name='excurri'),
    path('contest/', views.contest, name='contest'),
    path('test/', views.test, name="test"),
]