from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.

# we created a function (def) called post_list that takes request 
# and return a function render that will render (put together) our 
# template blog/post_list.html.
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})