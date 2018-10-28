# The views file connects models to templates

from django.shortcuts import render
from django.utils import timezone
#Import the model of the posts, so the parts it consists of (name, author, etc)
from .models import Post


# Create your views here.

def post_list(request):
    #Take the actual blog posts from the Post model and publish posts sorted by published_date
    #create a variable for QuerySet, named post. QuesrySet is called post.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #parameter request: everything we receive from the user via internet
    #parameter 'blog/post_list.html': giving the template file
    #parameter {}: place in which we can add some things for the template to use
    return render(request, 'blog/post_list.html', {'posts': posts})
    
