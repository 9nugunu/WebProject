from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from ..models import QnaModel

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