from django.http import Http404
from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
from django.views.generic import ListView

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_list(request):
    post_list = Post.published.all()
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except:
        posts = paginator.page(paginator.num_pages)
    return render(request,
                  'blog/post/list.html',
                  {'posts': posts})

def post_detail(request, id):
    try:
        post = Post.published.get(id = id)
    except Post.DoesNotExist:
        raise Http404("No Post found")
    return render (request,
                   'blog/post/detail.html',
                  {'post': post})