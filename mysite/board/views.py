from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm, CommentForm #PostForm가져오기. CommentForm가져오기
from django.http import HttpResponse
# Create your views here.

def home(request):      #'index' 페이지
    posts = Post.objects    #Post 객체들을 posts 변수에 저장
    return render(request, 'board/index.html', {'posts':posts})
    #board.index.html 가져오기 / posts호출 시 아까 posts에 담아준 Post의 object를 가져오기

def post_create(request):

    if request.method == 'POST':        #POST 방식이면, 데이터가 담긴 제출된 폼으로 간주
        form = PostForm(request.POST)   #request에 담긴 데이터로, 클래스 폼 생성
        if form.is_valid():             #폼에 담긴 데이터가 유효한지 체크
            form.save()                 #form에 저장  
            return  redirect('home')    #url = 'home'으로 되돌아가기
    else:
        form = PostForm()               #새 폼을 추가하기 위해 PostForm() 함수 호출 /
    return render(request, 'board/postcreate.html',{'form':form})

def post_detail(request, pk):           #pk :게시물 고유번호

    post = get_object_or_404(Post, pk=pk)           #object를 가져오거나 없으면 404에러

    return render(request,'board/postdetail.html',{'post':post})

def post_update(request, pk):           #수정하기
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)    #post 인스턴스를 받아서 그 안에 써 있는 내용 불러오기
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'board/postupdate.html',{'form':form})

def post_delete(request, pk):               #삭제기능
    post = Post.objects.get(pk=pk)          #get 방식으로 가져온 post.objects를 post에 담기
    post.delete()                           #delete함수
    return redirect('home')                 #완료되면 'home'으로 돌아가기

def comments(request, pk):                  #댓글기능 
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)    #넘겨진 데이터를 바로 Post모델에 저장하지 말라 
            comment.post = post                  #작성자 추가한 다음 저장
            comment.save()
            return redirect('detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'board/comment.html', {'form': form})