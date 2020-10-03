from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
#from .models import QnaModel
#from .forms import New

# Create your views here.

def QnA_main(request):
    return render(request, 'QnA_main.html')

#def read(request):
#    boards = QnaModel.objects.all()
#    return render(request, 'QnA_list.html', {'boards': boards})

#def writing(request):
#    if request.method == 'POST':
#        form = New(request.POST)
#        if form.is_valid:
###            post = form.save(commit=False)
 #           post.pub_date = timezone.now()
 #           post.save()
 #           return redirect('QnA_read')
 #   else:
 #       form = New()
 #       return render(request, 'QnA_writing.html', {'form':form})

def update(request, pk):
    return render(request, 'QnA_update.html')

#def delete(request, pk):
##    Remove = get_object_or_404(QnaModel, pk = pk)
 #   Remove.delete()
 #   return redirect('QnA_read.html')