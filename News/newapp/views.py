from datetime import datetime
from django.views.generic import ListView, DetailView,CreateView,UpdateView,DeleteView
from .models import *
from .forms import PostForm
from .filters import PostFilter
from django.urls import reverse_lazy


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'News.html'
    context_object_name = 'News'
    paginate_by = 2
    form_class =PostForm

class Post_Filter(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'search.html'
    context_object_name = 'News'
    paginate_by = 3
    form_class =PostForm


    def get_queryset(self):
        queryset=super().get_queryset()
        self.filterset=PostFilter(self.request.GET,queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['time_now'] = datetime.utcnow()
        context['filterset'] = self.filterset
        return context


class PostDetail(DetailView):
    model = Post
    template_name = 'New.html'
    context_object_name = 'New'

class PostCreate(CreateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def form_valid(self, form):
        Post = form.save(commit=False)
        Post.categoryType = 2
        return super().form_valid(form)

class PostUpdate(UpdateView):
    form_class = PostForm
    model = Post
    template_name = 'post_edit.html'

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)

class PostDelete(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('post_list')




