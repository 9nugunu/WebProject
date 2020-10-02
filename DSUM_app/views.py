from django.shortcuts import render

# Create your views here.

def dsum(request):
    return render(request, 'dsum.html')
    