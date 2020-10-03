from django.shortcuts import render, redirect, get_object_or_404, Http404
from django.utils import timezone
from .models import QnaModel
from .forms import New, AnswerForm

# Create your views here.

def QnA_main(request):
    boards = QnaModel.objects.all()
    return render(request, 'QnA_main.html', {'boards':boards})

def detail(request, pk):
    try:
        boards = get_object_or_404(QnaModel, pk=pk)
    except QnaModel.DoesNotExist:
        raise Http404("Does not exist!")
    return render(request, 'QnA_detail.html', {'boards': boards})

def post(request):
    if request.method == 'POST':
        form = New(request.POST)
        if form.is_valid:
            author = request.POST['author']
            title = request.POST['title']
            content = request.POST['content']
            docfile = request.POST['docfile']
            board = QnaModel(author=author, title=title, content=content, docfile=docfile)
            board.save()
            return redirect('QnA_main')
    else:
        form = New()
        return render(request, 'QnA_post.html', {'form':form})

def update(request, pk):
    return render(request, 'QnA_update.html')

def delete(request, pk):
    Remove = get_object_or_404(QnaModel, pk = pk)
    Remove.delete()
    return redirect('QnA_main')

def answer_create(request, pk):
    question = get_object_or_404(QnaModel, pk=pk)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('detail', pk=pk)
    else:
        form = AnswerForm()
    context = {'question': question, 'form': form}
    return render(request, 'QnA_detail.html', context)