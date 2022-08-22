from django.views import generic
from django.contrib import messages
from http.client import HTTPResponse
from post_image_app.forms import PostImageForm
from post_image_app.models import Post
from typing import Any


# Home page view
class HomePageView(generic.ListView):
    model = Post
    template_name: str = 'post_image_app/index.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-post_time')


# detail view for a post
class DetailPostView(generic.DetailView):
    model = Post
    template_name: str = 'post_image_app/detail.html' 


# psot a new image   
class NewPostView(generic.CreateView):
    model = Post
    form_class = PostImageForm
    # template_name: str = 'post_image_app/post_create_form.html'
    template_name_suffix: str = '_create_form'
    success_url: str = '/'
    
    def form_valid(self, form) -> HTTPResponse:
        messages.add_message(self.request, messages.INFO, 'Your Image was successfully uploaded.')
        return super().form_valid(form)