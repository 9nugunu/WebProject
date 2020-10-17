from django.db import models
from django.contrib.auth.models import User
 #Create your models here.

class QnaModel(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   title = models.CharField(max_length=100, null=False)
   content = models.TextField(null=False)
   docfile = models.FileField(default="", upload_to="document/upload/")
   created_date = models.DateTimeField(auto_now_add=True)
   modified_date = models.DateTimeField(auto_now=True)
   hits = models.PositiveIntegerField(default = 0)

   def __str__(self):
      return self.title
   
   @property
   def counter(self):
      self.hits = self.hits + 1
      self.save()


class Answer(models.Model):
   author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
   question = models.ForeignKey(QnaModel, on_delete=models.CASCADE)
   content = models.TextField(null=False)
   created_date = models.DateTimeField(auto_now_add=True)
   modified_date = models.DateTimeField(auto_now=True)