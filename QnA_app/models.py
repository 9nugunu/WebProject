from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
 #Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=30)
    parent = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        unique_together = ["category_name"]
    
    def __str__(self):
        return self.category_name

class QnaModel(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   title = models.CharField(max_length=100, null=False)
   content = RichTextUploadingField(null=False)
   created_date = models.DateTimeField(auto_now_add=True)
   modified_date = models.DateTimeField(null=True, blank=True)
   hits = models.PositiveIntegerField(default = 0)
   category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)

   def __str__(self):
      return self.title
   
   @property
   def counter(self):
      self.hits = self.hits + 1
      self.save()

class Answer(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   question = models.ForeignKey(QnaModel, on_delete=models.CASCADE)
   content = RichTextUploadingField(null=False)
   created_date = models.DateTimeField(auto_now_add=True)
   modified_date = models.DateTimeField(null=True, blank=True)

class Comment(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE)
   content = models.TextField()
   created_date = models.DateTimeField()
   modified_date = models.DateTimeField(null=True, blank=True)
   question = models.ForeignKey(QnaModel, null=True, blank=True, on_delete=models.CASCADE)
   answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)