# 웹사이트 개발시 사용자로부터 입력을 받기 위해서 폼을 사용
# 폼데이터를 어디로 보내는지 지정해주는 action 속성 과 어떤 HTTP 메소드로 보낼지 지정해주는 method속성 설정
#
#

from django import forms
from .models import Post, Comment

# form클래스 생성
class PostForm(forms.ModelForm):

    class Meta:             # 폼을 만들기 위해 어떤 model을 써야 하는지 
        
        model = Post
        fields = ['title','author','content'] 

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['c_author','c_content']
        labels = {
            'c_author':'글쓴이',
            'c_content':'내용',
                    }                # <label> elements 