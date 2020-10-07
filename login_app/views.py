from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from login_app.forms import UserForm
# Create your views here.

def signup(request):
    # post일 경우 사용자 생성
    if request.method == "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('QnA_main')
    else:
        form = UserForm()
    # get일 경우 홈페이지 호출
    return render(request, 'signup.html', {'form':form})

