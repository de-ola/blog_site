from django import forms
from .models import Blog, Category, Comment


choices = Category.objects.all().values_list('name', 'name')
choice = []
for item in choices:
    choice.append(item)

class CreateNewPost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'author', 'category', 'snippet', 'header_image', 'body', 'footer_image']
        widgets = {
            'title': forms.TextInput(),
            'author': forms.TextInput(attrs={'value':'', 'id':'blogger', 'type':'hidden'}),
            #'author': forms.Select(),
            'category':forms.Select(choices=choice),
            'snippet':forms.Textarea(attrs={'rows':15, 'col':45}),
            'body':forms.Textarea(attrs={'rows':15, 'col':45}),
        }

class UpdatePost(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ['title', 'snippet', 'body']
        widgets = {
            'title': forms.TextInput(),
            'snippet':forms.Textarea(attrs={'rows':15, 'col':45}),
            'body':forms.Textarea(attrs={'rows':15, 'col':45}),
        }

class CommentSection(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'comment']
        widgets = {
            'name': forms.TextInput(),
            'comment':forms.Textarea(attrs={'rows':10, 'col':25}),
        }
