from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.http import HttpResponse
from .models import Post

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']


class PostDetailView(DetailView):
    model = Post
   #post_detail.html


class PostCreateView(LoginRequiredMixin , CreateView):
    model = Post
    fields = ['title' , 'content']

    ## Permission to user own post only create post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin , UserPassesTestMixin , UpdateView):
    model = Post
    fields = ['title' , 'content']
    ## Permission to user own post only update post
    def form_valid(self , form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    ## Permission to user own post only update post
    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False

class PostDeleteView(LoginRequiredMixin , UserPassesTestMixin , DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author :
            return True
        return False


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
