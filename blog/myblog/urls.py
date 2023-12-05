from django.urls import path 
from . import views
from django.conf.urls.static import static
from .views import admin_data, HomeView,ArticleDetailView,AddPostView,UpdatePostView,DeletePostView,AddCategoryView,LikeView,AddCommentView
urlpatterns = [
  
   path('', HomeView.as_view(), name="home"),
   path('article/<int:pk>', ArticleDetailView.as_view(), name="article_details"),
   path('add_post/', AddPostView.as_view(),  name="add_post"),
   path('article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
   path('article/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
   path('add_category/', AddCategoryView.as_view(),  name="add_category"),
   path('like/<int:pk>', LikeView, name='like_post'),
   path('article/<int:pk>/comment/', AddCommentView.as_view(), name="add_comment"),
    path('admin_data/', admin_data, name='admin_data'),
    path('delete_user/<int:user_id>/', views.delete_user, name='delete_user'),
    path('delete_category/<int:category_id>/', views.delete_category, name='delete_category'),
    path('delete_comment/<int:comment_id>/', views.delete_comment, name='delete_comment'),






]

