# The views file connects models to templates

from django.shortcuts import redirect
from django.shortcuts import render
from django.utils import timezone
#Import the model of the posts, so the parts it consists of (name, author, etc)
from .models import Post
# when you ander a pk value that does not exist you get a nice error message 
from django.shortcuts import render, get_object_or_404
from .forms import PostForm


# views are below

def post_list(request):
    #Take the actual blog posts from the Post model and publish posts sorted by published_date
    #create a variable for QuerySet, named post. QuesrySet is called post.
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    #parameter request: everything we receive from the user via internet
    #parameter 'blog/post_list.html': giving the template file
    #parameter {}: place in which we can add some things for the template to use
    return render(request, 'blog/post_list.html', {'posts': posts})

#To see a single post/details of a post
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
    # Refers to the post_detail.html template

#View for new blog entries created inn the custom form
def post_new(request):
    if request.method == "POST": #If the method is POST(you want to post something),then construct the form
        form = PostForm(request.POST) #POST because you're posting data
        if form.is_valid(): #Check if all required fields in the form are set
            post = form.save(commit=False)
            post.author = request.user
            post.save() #if it's allvalid it can be saved
            return redirect('post_detail', pk=post.pk) #Go to post detail page of newlycreated page
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

#View to edit posts
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})

#View for list of draft posts
def post_draft_list(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date') #filter to only show unpublished posts, ordered by created date
    return render(request, 'blog/post_draft_list.html', {'posts': posts})

#View for publishing draft posts    
def post_publish(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

#View for deleting a post
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('post_list')