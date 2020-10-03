from django import forms
from .models import QnaModel, Answer
class New(forms.ModelForm):
    class Meta:
        model = QnaModel
        fields = ['title', 'content']

class AnswerForm(forms.ModelForm):
    class Meta:
       model = Answer
       fields = ['content']
       labels = {
           'content' : '답변내용',
       }
