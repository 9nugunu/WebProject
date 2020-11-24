from django import forms
from .models import QnaModel, Answer, Comment
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django_summernote.widgets import SummernoteWidget

class New(forms.ModelForm):
    class Meta:
        model = QnaModel
        fields = ['title', 'content']

    widgets = {
            'title': forms.TextInput(
                attrs={'class': 'form-control', 'style': 'width: 200%', 'placeholder': '제목을 입력하세요.'}
            ),
            'content': forms.CharField(widget=CKEditorUploadingWidget()),
        }

class AnswerForm(forms.ModelForm):
    class Meta:
       model = Answer
       fields = ['content']
       labels = {
       'content' : '답변내용',
       }
    widgets = {
        'content': forms.CharField(widget=CKEditorUploadingWidget()),
    }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }
