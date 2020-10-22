from django.urls import path
from . import views

urlpatterns = [
    path('', views.QnA_main, name="QnA_main"),
    path('post/', views.post, name="post"),
    path('detail/<int:pk>', views.detail, name="QnA_detail"),
    path('update/<int:pk>', views.question_update, name="question_update"),
    path('delete/<int:pk>', views.question_delete, name="question_delete"),
    path('answer/<int:pk>', views.answer_create, name='answer_create'),
]