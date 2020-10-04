from django.contrib import admin
from .models import QnaModel
# Register your models here.

# 관리자 화면에서 제목으로 검색하는 기능
class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(QnaModel, QuestionAdmin)