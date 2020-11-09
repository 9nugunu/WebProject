from django.urls import path
from . import views
from .views import base_views, question_views, answer_views, comment_views

app_name = 'QnA_app'

urlpatterns = [
    # base_views.py
    path('', base_views.QnA_main, name="QnA_main"),
    path('detail/<int:pk>', base_views.detail, name="QnA_detail"),

    # question_views.py
    path('post/', question_views.post, name="post"),
    path('question/update/<int:pk>', question_views.question_update, name="question_update"),
    path('delete/<int:pk>', question_views.question_delete, name="question_delete"),

    # answer_views.py
    path('answer/<int:pk>', answer_views.answer_create, name='answer_create'),
    path('answer/update/<int:answer_id>/', answer_views.answer_update, name='answer_update'),
    path('answer/delete/<int:answer_id>/', answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/question/<int:pk>/', comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/', comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/', comment_views.comment_delete_question, name='comment_delete_question'), 
    path('comment/create/answer/<int:answer_id>/', comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/', comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/', comment_views.comment_delete_answer, name='comment_delete_answer'),
]