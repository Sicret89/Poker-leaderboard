from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.edit import DeleteView
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.models import User
from .models import News


def home(request):
    context = {
        'posts': News.objects.all()
    }
    return render(request, 'core/home.html', context)

class PostListView(ListView):
    model = News
    template_name = 'core/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 6

class UserPostListView(ListView):
    model = News
    template_name = 'core/user_posts.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return News.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
    model = News

class PostCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = News
    fields = ['title', 'content']
    success_message = "Your post has been Created!"

    def create(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostUpdateView, self).update(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, UpdateView):
    model = News
    fields = ['title', 'content']
    success_message = "Your post has been Updated!"

    def update(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostUpdateView, self).update(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, SuccessMessageMixin, DeleteView):
    model = News
    success_url = '/'
    success_message = "Your post has been Deleted!"

    def delete(self, request, *args, **kwargs):
        messages.warning(self.request, self.success_message)
        return super(PostDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        else:
            return False

def about(request):
    return render(request, 'core/about.html', {'title': 'About'})
