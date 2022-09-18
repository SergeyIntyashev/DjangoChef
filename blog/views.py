from django.shortcuts import render
from django.views import generic

from blog.models import Post


class PostListView(generic.ListView):
    model = Post

    def get_queryset(self):
        return Post.objects. \
            select_related('category'). \
            filter(category__slug=self.kwargs.get('slug'))


def home(request):
    return render(request, 'base.html')
