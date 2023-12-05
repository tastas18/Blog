from django.urls import path 
from .views import UserRegisterView, UserEditView,ShowProfilePageView,EditProfilePageView,CustomLoginView
from django.contrib.auth import views as auth_views
from .views import EditProfilePageView
urlpatterns = [
 path('register/', UserRegisterView.as_view(),name='register'),
 path('edit_profile/',  UserEditView.as_view(), name='edit_profile'),
 path('<int:pk>/profile/', ShowProfilePageView.as_view(), name='show_profile_page'),
 path('<int:pk>/edit_profile_page/', EditProfilePageView.as_view(), name='edit_profile_page'),
 path('/memebres/login/', CustomLoginView.as_view(), name='login'),


]
