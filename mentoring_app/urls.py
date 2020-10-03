from django.urls import path
from . import views

urlpatterns = [
    path('dsum/', views.dsum, name='dsum'),
    path('tutoring/', views.tutoring, name='tutoring'),
]
