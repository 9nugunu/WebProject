from django.db import models

# Create your models here.

class Write_list(models.Model):
   title = models.CharField(max_length=100, null=False)
   image = models.ImageField(upload_to='images/')
   created_date = models.DateTimeField(auto_now_add=True)
   end_date = models.DateTimeField()
   hits = models.PositiveIntegerField(default = 0)
   link = models.URLField("Site URL", null=False, blank=False, max_length=200)

   def __str__(self):
      return self.title
   
   @property
   def counter(self):
      self.hits = self.hits + 1
      self.save()