from django.shortcuts import render

# Create your views here.

def tutoring(request):
    return render(request, 'tutoring.html')