from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from ..forms import New
from ..models import QnaModel

@login_required(login_url='login_app:login')
def post(request):
    if request.method == 'POST':
        form = New(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.created_date = timezone.now()
            question.save()
            return redirect('QnA_app:QnA_main')
    else:
        form = New()
    context = {'form': form}
    return render(request, 'QnA/QnA_post.html', context)
    
@login_required(login_url='login_app:login')
def question_update(request, pk):
    question = get_object_or_404(QnaModel, pk=pk)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('QnA_app:QnA_detail', pk=question.id)

    if request.method == "POST":
        form = New(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modified_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('QnA_app:QnA_detail', pk=question.id)
    else:
        form = New(instance = question)
    context = {'form': form}
    return render(request, 'QnA/QnA_question_update.html', context)

@login_required(login_url='login_app:login')
def question_delete(request, pk):
    question = get_object_or_404(QnaModel, pk=pk)
    if request.user != question.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('QnA/QnA_detail.html', pk=question.id)
    question.delete()
    return redirect('QnA_app:QnA_main')