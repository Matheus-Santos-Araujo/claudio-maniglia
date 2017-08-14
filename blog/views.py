from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .models import Type

def base(request):
    tags = Type.objects.all()
    return render(request, 'blog/base.html', {'tags': tags})
def post_list(request):
    tags = Type.objects.all()
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'blog/post_list.html', {'posts': posts, 'tags': tags})
