from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    # post/: URL should begin with post/
    # <int:pk>: after post/ django expects an integer (the unique name for each blog post in the database)
    # django will transfer the integer to a view as a variable called pk
    # at http://127.0.0.1:8000/post/5/ django knows you look for a view called post_detail and transfers the information that pk=5 to that view
    # next: add the view in views.py
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]