from django import forms
from django.forms import ModelForm
from blogs.models import Article
from django.core.exceptions import ValidationError
def word_num_validator(number):
    if len(number) < 4:
        raise ValidationError


class NewBlogForm(forms.Form):
    title = forms.CharField(
        label="标题:",
        max_length=100,
        validators=[word_num_validator],

    )
    blog_degist = forms.CharField(
        label="摘要",
        max_length=200,
        widget=forms.Textarea
    )
    blog_content = forms.CharField(
        label="内容:",
        widget=forms.Textarea,
        error_messages= {
            "required":'字数过少'
        },
        validators=[word_num_validator]
    )

#从models中导入的Form,fields选择性暴露html的接口
class ArticleForm(ModelForm):
    class Meta:
        model = Article
        # fields = "__all__"
        fields = ['articler','article_content'] #暴露给form的接口
