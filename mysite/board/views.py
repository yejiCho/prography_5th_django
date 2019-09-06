from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from .models import Post
from .forms import PostForm, CommentForm
from django.http import HttpResponse
# Create your views here.

def home(request):
    posts = Post.objects
    return render(request, 'board/index.html', {'posts':posts})

def post_create(request):

    if request.method == 'POST':        #POST 방식이면, 데이터가 담긴 제출된 폼으로 간주
        form = PostForm(request.POST)   #request에 담긴 데이터로, 클래스 폼 생성
        if form.is_valid():             #폼에 담긴 데이터가 유효한지 체크
            form.save()                 
            return  redirect('home')
    else:
        form = PostForm()               #새 폼을 추가하기 위해 PostForm() 함수 호출
    return render(request, 'board/postcreate.html',{'form':form})

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)           #장고 단축함수 /함수를 임포트 하도록 

    return render(request,'board/postdetail.html',{'post':post})

def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = PostForm(instance=post)
    return render(request, 'board/postupdate.html',{'form':form})

def post_delete(request, pk):
    post = Post.objects.get(pk=pk)
    post.delete()
    return redirect('home')

def comments(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=pk)
    else:
        form = CommentForm()
    return render(request, 'board/comment.html', {'form': form})