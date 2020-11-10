from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect, resolve_url
from django.utils import timezone

from ..forms import CommentForm
from ..models import QnaModel, Answer, Comment

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
            return redirect('{}#comment_{}'.format(
                resolve_url('QnA_app:QnA_detail', pk=question.id),
                comment.id))
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
            return redirect('{}#comment_{}'.format(
                resolve_url('QnA_app:QnA_detail', pk=comment.question.id),
                comment.id))
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'QnA/comment_form.html', context)

@login_required(login_url='login_app:login')
def comment_delete_question(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글삭제권한이 없습니다')
        return redirect('QnA_app:QnA_detail', pk=comment.pk)
    else:
        comment.delete()
    return redirect('QnA_app:QnA_detail', pk=comment.pk)

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
            return redirect('{}#comment_{}'.format(
                resolve_url('QnA_app:QnA_detail', pk=comment.answer.question.id),
                comment.id))
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'QnA/comment_form.html', context)


@login_required(login_url='common:login')
def comment_modify_answer(request, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.user != comment.author:
        messages.error(request, '댓글수정권한이 없습니다')
        return redirect('QnA_app:QnA_detail', pk=comment.answer.question.id)

    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.modified_date = timezone.now()
            comment.save()
            return redirect('{}#comment_{}'.format(
                resolve_url('QnA_detail', pk=comment.answer.question.id),
                comment.id))
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