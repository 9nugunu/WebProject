from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.utils import timezone
from django.core.paginator import Paginator
from .models import QnaModel, Answer, Comment
from .forms import New, AnswerForm, CommentForm
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
            question.author = request.user
            question.created_date = timezone.now()
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
            answer.created_date = timezone.now()
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
            question.modified_date = timezone.now()  # 수정일시 저장
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

@login_required(login_url='login_app:login')
def answer_update(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('QnA_detail', pk=answer.question.id)

    if request.method == "POST":
        form = AnswerForm(request.POST, instance=answer)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.author = request.user
            answer.modified_date = timezone.now()
            answer.save()
            return redirect('QnA_detail', pk=answer.question.id)
    else:
        form = AnswerForm(instance=answer)
    context = {'answer': answer, 'form': form}
    return render(request, 'QnA/QnA_answer_update.html', context)

@login_required(login_url='login_app:login')
def answer_delete(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.user != answer.author:
        messages.error(request, '삭제권한이 없습니다')
    else:
        answer.delete()
    return redirect('QnA_detail', pk=answer.question.id)

############################################################################
@login_required(login_url='login_app:login')
def comment_create_question(request, pk):
    question = get_object_or_404(QnaModel, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.created_date = timezone.now()
            comment.question = question
            comment.save()
            return redirect('QnA_detail', pk=question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'QnA/comment_form.html', context)

@login_required(login_url='login_app:login')
def comment_modify_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('pybo:detail', pk=comment.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modified_date = timezone.now()
            comment.save()
            return redirect('QnA_detail', pk=comment.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'QnA/comment_form.html', context)

@login_required(login_url='login_app:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('QnA_detail', pk=comment.pk)
    else:
        comment.delete()
    return redirect('QnA_detail', pk=comment.pk)

@login_required(login_url='login_app:login')
def comment_create_answer(request, answer_id):
    answer = get_object_or_404(Answer, pk=answer_id)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.created_date = timezone.now()
            comment.answer = answer
            comment.save()
            return redirect('QnA_detail', pk=comment.answer.question.id)
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'QnA/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('QnA_detail', pk=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modified_date = timezone.now()
            comment.save()
            return redirect('QnA_detail', pk=comment.answer.question.id)
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'QnA/comment_form.html', context)


@login_required(login_url='login_app:login')
def comment_delete_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('QnA_detail', pk=comment.answer.question.id)
    else:
        comment.delete()
    return redirect('QnA_detail', pk=comment.answer.question.id)