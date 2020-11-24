from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.db.models import Q, Count
from ..models import QnaModel

def QnA_main(request):
    """
    paginator
    """
    # 입력 parameter
    page = request.GET.get('page', '1')
    search_menu = request.GET.get('search_menu', '') # 검색 종류
    search = request.GET.get('search', '')  # 검색어
    so = request.GET.get('so', 'recent')  # 정렬기준

    # 정렬
    if so == 'recent':
        boards = QnaModel.objects.order_by('-created_date')
    elif so == 'author':
        boards = QnaModel.objects.order_by('author', '-created_date')
    else:  # popular
        boards = QnaModel.objects.order_by('-hits')
    
    #------------------------------------------------------------------------#
    # 검색
    if search:
        if search_menu == 'title':
            boards = boards.filter(
                Q(title__icontains=search)  # 제목검색
                #Q(content__icontains=kw) |  # 내용검색
                #Q(author__username__icontains=kw) |  # 질문 글쓴이검색
                #Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색 
            ).distinct()

        elif search_menu == 'content':
            boards = boards.filter(
                #Q(title__icontains=search)  # 제목검색
                Q(content__icontains=search) # 내용검색
                #Q(author__username__icontains=kw) |  # 질문 글쓴이검색
                #Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색 
            ).distinct()
        
        else:
            boards = boards.filter(
                #Q(title__icontains=search)  # 제목검색
                #Q(content__icontains=search) # 내용검색
                Q(author__username__icontains=search) # 질문 글쓴이검색
                #Q(answer__author__username__icontains=kw)  # 답변 글쓴이검색 
            ).distinct()
    #------------------------------------------------------------------------#

    # 페이징 처리
    paginator = Paginator(boards, 10) # 게시글 10개
    page_obj = paginator.get_page(page)

    context = {'boards': page_obj, 'page': page, 'search': search, 'search_menu': search_menu, 'so': so}  # page와 search가 추가되었다.
    # boards = QnaModel.objects.all()
    return render(request, 'QnA/QnA_main.html', context)

def detail(request, pk):
    try:
        boards = get_object_or_404(QnaModel, pk=pk)
    except QnaModel.DoesNotExist:
        raise Http404("Does not exist!")
    boards.counter
    return render(request, 'QnA/QnA_detail.html', {'boards': boards})