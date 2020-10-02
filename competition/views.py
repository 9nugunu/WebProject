from django.shortcuts import render

# Create your views here.

def competition(request):
    return render(request, 'competition.html')
    