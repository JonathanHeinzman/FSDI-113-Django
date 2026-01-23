# from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post, Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy

# Create your views here.
class PostDraftListView(ListView):
    """
    PostDraftListView is going to help us to display all posts from the db with a Draft status
    """
    template_name = "posts/draft.html"
    context_object_name = "drafts"
    draft_status = Status.objects.get(name="Draft")
    queryset = Post.objects.filter(status=draft_status).order_by("created_on").reverse()


class PostArchivedListView(ListView):
    """
    PostArchivedListView is going to help us to display all posts from the db with a Archived status
    """
    template_name = "posts/archived.html"
    context_object_name = "archived"
    archived_status = Status.objects.get(name="Archived")
    queryset = Post.objects.filter(status=archived_status).order_by("created_on").reverse()


class PostListView(ListView): 
    """
    PostListView is going to retrieve all of the objects from the Post table in the database
    """
    template_name = "posts/list.html"
    #model = Post
    context_object_name = "post"
    published_status = Status.objects.get(name="Published")
    #Queryset attribute allow us to select some data from the db using the model class
    queryset = Post.objects.filter(status=published_status).order_by("created_on").reverse()


class PostDetailView(DetailView): 
    """
    PostDetailView is going to retrieve a single element from the Post table in the db.
    """
    template_name = "posts/detail.html"
    model = Post
    context_object_name = "single_post"


class PostCreateView(CreateView): # POST
    """
    PostCreateView is going to allow us to create a new post and add it to the db
    """
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        print(User.objects.all())
        form.instance.author = User.objects.last() 
        return super().form_valid(form)
    
class PostUpdateView(UpdateView):
    """
    PostUpdateView allows us to update an existing record from the db
    """
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle","body"]

class PostDeleteView(DeleteView):
    """
    PostDeleteView allows us to delete an existing record from the db
    """

    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")