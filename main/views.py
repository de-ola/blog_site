from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Blog, Category, Comment, Profile
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import CommentSection, CreateNewPost, UpdatePost
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required


# Create your views here.
class index(ListView):
    model = Blog
    template_name = 'main/index.html'
    ordering = ['-created_at']

def blogpost(response, pk):
    blog = Blog.objects.get(id=pk)
    if response.method == "POST":
        form = CommentSection(response.POST)
        if form.is_valid():
            n = form.cleaned_data["name"]
            c = form.cleaned_data["comment"]
            blog.comments.create(name=n, comment=c)
            return HttpResponseRedirect("/%i" %blog.id)
        else:
            print("invalid code")

    else:
        form = CommentSection()
    return render(response, 'posts/post.html', {'blog':blog, 'form':form})

class update(UpdateView):
    model = Blog
    template_name = 'posts/update.html'
    form_class = UpdatePost

class create(CreateView):
    model = Blog
    template_name = 'main/create.html'
    form_class = CreateNewPost
    success_url = reverse_lazy('index')

class delete(DeleteView):
    model = Blog
    template_name = 'posts/delete.html'
    success_url = reverse_lazy('index')
