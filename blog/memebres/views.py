from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import DetailView, CreateView
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.urls import reverse_lazy
from .forms import SignUpForm,EditProfileForm
from django.views.generic import UpdateView
from myblog.models import Profile
from django.views.generic import DetailView
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect

class CustomLoginView(LoginView):
    def get_success_url(self):
        redirect_to = super().get_success_url()
        if self.request.user.username == 'admin':
            redirect_to = '/admin_data/'  # Redirige vers la page admin_data
        return redirect_to

from .forms import CustomUserCreationForm

class UserRegisterView(generic.CreateView):
    form_class = CustomUserCreationForm 
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserRegisterView(generic.CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')



class UserEditView(generic.UpdateView):
    form_class = EditProfileForm
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

    def get_object(self):
        return self.request.user



class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(*args, **kwargs)

        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])

        context["page_user"] = page_user
        return context

class EditProfilePageView(generic.UpdateView):
    model = Profile
    template_name = 'registration/edit_profile_page.html'
    fields = ['bio', 'profile_pic',  'instagram_url', 'pinterest_url']
    success_url = reverse_lazy('home')
