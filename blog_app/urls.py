"""Defines URL patterns for todo_app"""

from hashlib import new
from django.urls import path

from . import views

app_name = 'blog_app'

urlpatterns = [
    # Home page
    path('', views.index, name='index'),
    
    # Show all posts
    path('posts/', views.posts, name= 'posts'),
    
    # View individual post
    path('posts/<int:post_id>/', views.post, name='post'),
    
    # Create new post
    path('create_post/', views.create_post, name = 'create_post'),
    
    # Edit a post
    path('posts/<int:post_id>/edit/', views.edit_post, name='edit_post'),
    
    # Delete a post
    path('posts/<int:post_id>/delete', views.delete_post, name='delete_post'),
    
    # create a new entry
    path('posts/<int:post_id>/new_entry/', views.create_entry, name='new_entry'),
    
    # Edit an entry.
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
    # delete an entry
    path('entry_delete/<int:entry_id>/', views.delete_entry, name='delete_entry'),

]
