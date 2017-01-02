from django import forms
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
    blog_content = forms.CharField(
        label="内容:",
        widget=forms.Textarea,
        error_messages= {
            "required":'字数过少'
        },
        validators=[word_num_validator]
    )
