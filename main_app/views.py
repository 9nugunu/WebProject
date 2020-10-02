from django.shortcuts import render

# Create your views here.

def main(request):
    return render(request, 'main.html')

def excurri(request):
    return render(request, 'excurri.html')

def contest(request):
    return render(request, 'contest.html')