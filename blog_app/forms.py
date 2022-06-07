from django import forms

from .models import Post, Entry

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title']
        
class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ['text']        
        