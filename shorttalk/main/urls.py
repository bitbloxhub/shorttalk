from django.urls import path

from shorttalk.main.views import AllPostListView, UserPostView, SetEmailView

urlpatterns = [
    path('', AllPostListView.as_view(), name = 'AllPostListView'),
    path('set_email', SetEmailView.as_view(), name = 'SetEmailView'),
    path('user_posts/<int:id>', UserPostView.as_view(), name = 'UserPostView')
]
