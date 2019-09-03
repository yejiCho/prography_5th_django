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

    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return  redirect('home')
    else:
        form = PostForm()
    return render(request, 'board/postcreate.html',{'form':form})

def post_detail(request, pk):

    post = get_object_or_404(Post, pk=pk)

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
    return render(request, 'board/addcomment.html', {'form': form})