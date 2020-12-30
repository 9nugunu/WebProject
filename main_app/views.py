from django.shortcuts import render
from .models import Write_list
from django.core.paginator import Paginator
# Create your views here.

def test(request):
    return render(request, 'test.html')
    
def main(request):
    WriteDsum = Write_list.objects
    return render(request, 'main/main.html', {'WriteDsum': WriteDsum})

def excurri(request):
    return render(request, 'excurri.html')

def contest(request):
    return render(request, 'contest.html')

def dsum(request):

    # 입력 파라미터
    page = request.GET.get('page', '1')  # 페이지
# ---------------------------------------------------------------------------- #    

    # 조회
    WriteDsum = Write_list.objects.order_by('-created_date')

    # 페이징처리
    paginator = Paginator(WriteDsum, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)

    context_dsum = {'WriteDsum': page_obj}
    return render(request, 'd-sum/dsum.html', context_dsum)
    
def tutoring(request):
    return render(request, 'tutoring.html')