from django import forms
from .models import Post, Comment

class PostForm(forms.ModelForm):

    class Meta:
        
        model = Post
        fields = ['title','author','content'] 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['c_author','c_content']
        labels = {
            'c_author':'글쓴이',
            'c_content':'내용',
                    }