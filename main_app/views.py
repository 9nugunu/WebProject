from django.shortcuts import render

# Create your views here.

def test(request):
    return render(request, 'test.html')
    
def main(request):
    return render(request, 'main.html')

def excurri(request):
    return render(request, 'excurri.html')

def contest(request):
    return render(request, 'contest.html')