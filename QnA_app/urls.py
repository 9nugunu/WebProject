from django.urls import path
from . import views

urlpatterns = [
    path('', views.QnA_main, name="QnA_main"),
    path('post/', views.post, name="post"),
    path('detail/<int:pk>', views.detail, name="QnA_detail"),
    path('question/update/<int:pk>', views.question_update, name="question_update"),
    path('delete/<int:pk>', views.question_delete, name="question_delete"),
    path('answer/<int:pk>', views.answer_create, name='answer_create'),
    path('answer/update/<int:answer_id>/', views.answer_update, name='answer_update'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('comment/create/question/<int:pk>/', views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', views.comment_delete_question, name='comment_delete_question'), 
    path('comment/create/answer/<int:answer_id>/', views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', views.comment_delete_answer, name='comment_delete_answer'),
]