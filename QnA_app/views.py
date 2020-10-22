from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import QnaModel
from .forms import New, AnswerForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def QnA_main(request):
    """
    paginator
    """
    # 입력 parameter
    page = request.GET.get('page', '1')

    # 조회
    boards = QnaModel.objects.order_by('-created_date')

    # 페이징 처리
    paginator = Paginator(boards, 10) # 게시글 10개
    page_obj = paginator.get_page(page)

    context = {'boards': page_obj}
    # boards = QnaModel.objects.all()
    return render(request, 'QnA/QnA_main.html', context)

def detail(request, pk):
    try:
        boards = get_object_or_404(QnaModel, pk=pk)
    except QnaModel.DoesNotExist:
        raise Http404("Does not exist!")
    boards.counter
    return render(request, 'QnA/QnA_detail.html', {'boards': boards})

@login_required(login_url='login_app:login')
def post(request):
    if request.method == 'POST':
        form = New(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user  # 추가한 속성 author 적용
            question.create_date = timezone.now()
            question.save()
            return redirect('QnA_main')
    else:
        form = New()
    context = {'form': form}
    return render(request, 'QnA/QnA_post.html', context)

def update(request, pk):
    return render(request, 'QnA/QnA_update.html')

def delete(request, pk):
    Remove = get_object_or_404(QnaModel, pk = pk)
    Remove.delete()
    return redirect('QnA_main')

@login_required(login_url='login_app:login')
def answer_create(request, pk):
    question = get_object_or_404(QnaModel, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('QnA_detail', pk=pk)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'QnA/QnA_detail.html', context)

@login_required(login_url='login_app:login')
def question_update(request, pk):
    question = get_object_or_404(QnaModel, pk=pk)
    if request.user != question.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('QnA_detail', pk=question.id)

    if request.method == "POST":
        form = New(request.POST, instance=question)
        if form.is_valid():
            question = form.save(commit=False)
            question.author = request.user
            question.modify_date = timezone.now()  # 수정일시 저장
            question.save()
            return redirect('QnA_detail', pk=question.id)
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
    return redirect('QnA_main')