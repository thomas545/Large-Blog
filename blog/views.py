from django.shortcuts import render , get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from django.http import HttpResponse
from .models import Post
## Django Rest Framework ##
from rest_framework import viewsets , permissions
from .serializers import PostSerializer , UserSerializer

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 5


class UserPostListView(ListView):
    model = Post
    template_name = 'blog/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 5

    # function to retrive users posts only
    def get_queryset(self):
        user = get_object_or_404(User , username=self.kwargs.get('username')) # username parameter = url virable like pk
        return Post.objects.filter(author=user).order_by('-date_posted')



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

## Django Rest Framework

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
