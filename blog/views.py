from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects. \
            select_related('category'). \
            filter(category__slug=self.kwargs.get('slug'))


class PostDetailView(generic.DetailView):
    model = Post
    slug_url_kwarg = 'post_slug'
    context_object_name = "post"


def home(request):
    return render(request, 'base.html')
