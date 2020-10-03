from django.urls import path
from . import views

urlpatterns = [
    path('', views.QnA_main, name="QnA_main"),
    path('post/', views.post, name="post"),
    path('detail/<int:pk>', views.detail, name="detail"),
    path('update/<int:pk>', views.update, name="update"),
    path('del/<int:pk>', views.delete, name="delete"),
    path('answer/<int:pk>', views.answer_create, name='answer_create'),
]