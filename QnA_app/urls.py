from django.urls import path
from . import views

urlpatterns = [
    path('', views.QnA_main, name="QnA_main"),
    path('read/', views.read, name="read"),
    path('write/', views.writing, name="writing"),
    path('update/<int:pk>', views.update, name="update"),
    path('del/<int:pk>', views.delete, name="delete"),
]