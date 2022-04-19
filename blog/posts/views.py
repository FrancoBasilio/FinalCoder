from email import message
from django.shortcuts import redirect, render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from requests import post
from posts.models import Post, Like, PostView
from .forms import PostForm, CommentsForm
from django.contrib.auth.forms import UserCreationForm



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            message.succes(request, f'User {username} create')
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'register.html', context)
class PostListView(ListView):
    model = Post

class PostDetailView(DetailView):
    model = Post
    
    def get_object(self, **kwargs):
        object = super().get_object(**kwargs)
        if self.request.user.is_authenticated:
            PostView.objects.get_or_create(user=self.request.user, post=object)
        return object
    
    def post(self, *args, **kwargs):
        form = CommentsForm(self.request.POST)
        if form.is_valid():
            post = self.get_object()
            comment = form.instance
            comment.user = self.request.user
            comment.post = post
            # comment.save()
            return redirect('detail', slug=post.slug)
        return redirect('detail', slug=self.get_object())
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'form': CommentsForm()
        })
        return context

class PostCreateView(CreateView):
    form_class = PostForm
    model = Post
    success_url = '/'
   
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'view_type': 'Create'
        })
        return context
    

class PostUpdateView(UpdateView):
    form_class = PostForm
    model = Post
    success_url = '/'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)  
        context.update({
            'view_type': 'Update'
        })  
        return context
    
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'

def like(request, slug):
    post = get_object_or_404(Post, slug=slug)
    like_qs = Like.objects.filter(user=request.user, post=post)
    if like_qs.exists():
        like_qs[0].delete()
        return redirect('detail',slug=slug)
    Like.objects.create(user=request.user, post=post)
    return redirect('detail',slug=slug)
