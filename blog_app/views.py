# from os import RWF_APPEND
import re
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

# Create your views here.

from .models import Post, Entry
from .forms import EntryForm, PostForm

def index(request):
    '''home page for Blog_app'''
    return render(request, 'blog_app/index.html')

# @login_required
def posts(request):
    '''show all posts'''
    posts = Post.objects.order_by('date_added')
    context = {'posts': posts}
    return render(request, 'blog_app/posts.html', context)


def post(request, post_id):
    '''show a single post and all its entries.'''
    post = get_object_or_404(Post, id=post_id)
    # Make sure the topic belongs to the current user.
    # if post.owner != request.user:
    #     raise Http404
    entries = post.entry_set.order_by('-date_added')
    context = {'post': post, 'entries': entries}
    return render(request, 'blog_app/post.html', context)


@login_required
def create_post(request):
    '''create a new post'''
    if request.method != 'POST':
        form = PostForm()
    else:
        form = PostForm(data=request.POST)
        if form.is_valid():
            new_post = form.save(commit=False)
            new_post.owner = request.user
            new_post.save()
            return redirect ('blog_app:posts')
        
    context = {'form': form}
    return render(request, 'blog_app/create_post.html', context)


@login_required
def edit_post(request, post_id):
    '''edit an existing post'''
    post = Post.objects.get(id=post_id)
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        '''Initial request; pre-fill form with the current post'''
        form = PostForm(instance=post)

    else:
        # POST data submitted; process data.
        form = PostForm(instance=post, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:post', post_id=post.id)

    context = {'post': post, 'form': form}
    return render(request, 'blog_app/edit_post.html', context)


@login_required
def delete_post(request, post_id):
    post = Post.objects.get(id=post_id)
    context = {'post': post}

    if request.method == "POST":
        post.delete()
        return redirect('blog_app:posts')

    return render(request, "blog_app/delete_post.html", context)


@login_required
def create_entry(request, post_id):
    '''create a new entry for a particular post.'''
    post = Post.objects.get(id=post_id)
    
    if request.method != 'POST':
        # No data submitted; create a blank form
        form = EntryForm()
        
    else:
        # POST data submitted; PROCESS data
        form = EntryForm(data=request.POST)
        if form.is_valid():
            create_entry = form.save(commit=False)
            create_entry.post = post
            create_entry.save()
            return redirect('blog_app:post', post_id=post_id)
        
    # Display a blank or invalid form.
    context = {'post': post, 'form': form}
    return render(request, 'blog_app/create_entry.html', context)            


@login_required
def edit_entry(request, entry_id):
    '''edit an existing entry.'''
    entry = Entry.objects.get(id=entry_id)
    post = entry.post
    if post.owner != request.user:
        raise Http404

    if request.method != 'POST':
        '''Initial request; pre-fill form with the current entry'''
        form = EntryForm(instance=entry)
        
    else:
        # POST data submitted; process data.
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('blog_app:post', post_id=post.id)
    
    context = {'entry': entry, 'post': post, 'form': form}
    return render(request, 'blog_app/edit_entry.html', context)


@login_required
def delete_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    context = {'entry': entry}
    post = entry.post
    if post.owner != request.user:
        raise Http404

    if request.method == "POST":
        entry.delete()
        return redirect('blog_app:post', post_id=post.id)

    return render(request, "blog_app/delete_entry.html", context)







