from django.urls import path
from post_image_app.views import DetailPostView, NewPostView, HomePageView

app_name = 'post_image_app'

urlpatterns = [
    #  /
    path('', HomePageView.as_view(), name='index'),
    #  /1/detail/
    path('<int:pk>/detail/', DetailPostView.as_view(), name='detail'),
    #  /1/detail/
    path('new_post/', NewPostView.as_view(), name='new_post'),
]