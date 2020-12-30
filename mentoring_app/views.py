from django.shortcuts import render
from .models import Write_mentoring
# Create your views here.

def dsum(request):
    WriteDsum = Write_mentoring.objects
    return render(request, 'dsum.html', {'WriteDsum': WriteDsum})
    
def tutoring(request):
    return render(request, 'tutoring.html')