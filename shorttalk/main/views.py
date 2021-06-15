from shorttalk.main.models import Post
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

# Create your views here.

class AllPostListView(ListView):
    template_name = 'all_posts.html'
    queryset = Post.objects.order_by('-id')
    paginate_by = 50

class UserPostView(ListView):
    template_name = 'user_posts.html'
    def get_queryset(self):
        return Post.objects.filter(author = User.objects.filter(id = self.kwargs['id'])[0])
    paginate_by = 50

class SetEmailView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    template_name = 'set_email.html'
    login_url = "/accounts/login"
    fields = ['email']
    def get_object(self, queryset = None):
        return self.request.user
    success_url = '/'
    success_message = 'Your email has been set'
