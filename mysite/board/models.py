from django.db import models

# Create your models here.

class Post(models.Model):       #게시글
    objects = models.Manager()  #class has no objects member 에러 해결
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)  #시간 자동으로 받아오기
    content = models.TextField(default='')  #default='' 공백

    def __str__(self):
        return self.title

class Comment(models.Model):        #댓글
    post = models.ForeignKey('board.Post', related_name='comments', on_delete=models.CASCADE)
    c_author = models.CharField(max_length=100, default="익명")
    c_content = models.TextField(default='')
    c_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.c_content
