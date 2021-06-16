from django.urls import path

from shorttalk.main.views import AllPostListView, UserPostView, NewPostView, SetEmailView

urlpatterns = [
    path('', AllPostListView.as_view(), name = 'AllPostListView'),
    path('user_posts/<int:id>', UserPostView.as_view(), name = 'UserPostView'),
    path('create_post', NewPostView.as_view(), name = 'NewPostView'),
    path('set_email', SetEmailView.as_view(), name = 'SetEmailView'),
]
