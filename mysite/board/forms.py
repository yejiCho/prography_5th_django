# 웹사이트 개발시 사용자로부터 입력을 받기 위해서 폼을 사용
# 폼데이터를 어디로 보내는지 지정해주는 action 속성 과 어떤 HTTP 메소드로 보낼지 지정해주는 method속성 설정
# ModelForm을 쓰면 일반 Form을 쓸 때 보다 할 일이 줄어든다. label이름 등 수정할게 없다면 ModelForm사용
# ModelForm을 생성해 자동으로 결과물 저장

from django import forms
from .models import Post, Comment

# form클래스 생성
class PostForm(forms.ModelForm):    

    class Meta:             # 폼을 만들기 위해 어떤 model을 써야 하는지 
        
        model = Post        #model에 정의된 class Post에서
        fields = ['title','author','content']   #사용자로부터 적어준 field데이터 직접 입력

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['c_author','c_content']
        labels = {
            'c_author':'글쓴이',
            'c_content':'내용',
                    }                # <label> elements 
                                     #필드가 양식에 표시될때 사용