from django import forms
from django.forms import ModelForm, TextInput, ImageField, Select, Textarea
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from pages.models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        exclude = ['slug']
        fields = ['title', 'image', 'category','body']
        body = forms.CharField(widget=CKEditorUploadingWidget())
        widgets = {
            'title': TextInput(attrs={
                'class': "form-input pl-12",               
                'placeholder': 'Title'
                }), 
            'category': Select(attrs={
                'class': "form-input pl-12",               
                'placeholder': 'Title'
                }),            
            'body': Textarea(attrs={
                'class': "form-input pl-11 h-28",
                'placeholder': 'Body',
                'width': '100% !important'
                })
        }
