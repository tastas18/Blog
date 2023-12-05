from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Category,Comment
from .forms import PostForm, EditForm ,CommentForm
from django.urls import reverse_lazy,reverse
# Create your views here.
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

def admin_data(request):
    posts = Post.objects.all()
    categories = Category.objects.all()
    comments = Comment.objects.all()
    users = User.objects.all()

    return render(request, 'admin_data.html', {
        'posts': posts,
        'categories': categories,
        'comments': comments,
        'users': users,
    })

def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


def index (request):
    return render (request, 'index.html',{})
class HomeView(ListView):
    model = Post
    template_name = 'home.html'
   
class ArticleDetailView(DetailView):
    model = Post
    template_name = 'article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context





class AddPostView(CreateView):
    model = Post
    form_class = PostForm  # Utilisez PostForm comme formulaire pour cette vue
    template_name = 'add_post.html'  # Assurez-vous que le nom de votre modèle est correct
    # Autres attributs de la vue...


class AddCategoryView(CreateView):
     model = Category
     template_name = 'add_category.html'
     fields = '__all__'



class UpdatePostView(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'update_post.html'
    #fields = ['title', 'category','title_tag', 'body']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')

class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'add_comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)

    success_url = reverse_lazy('home')



@login_required
def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    if request.method == 'POST':
        user.delete()
        # Rediriger vers une page de confirmation ou ailleurs après la suppression
        return redirect('admin_data')  # Redirige vers une vue où les données sont affichées
    # Si la méthode HTTP n'est pas POST, affichez une page de confirmation ou retournez une autre réponse

@login_required
def delete_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    if request.method == 'POST':
        category.delete()
        # Rediriger vers une page de confirmation ou ailleurs après la suppression
        return redirect('admin_data')  # Redirige vers une vue où les données sont affichées
    # Si la méthode HTTP n'est pas POST, affichez une page de confirmation ou retournez une autre réponse

# Ajoutez des vues pour d'autres modèles si nécessaire
@login_required
def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.method == 'POST':
        comment.delete()
        return redirect('admin_data')  # Redirige vers une vue où les données sont affichées
    # Gérer d'autres cas ou méthodes HTTP si nécessaire
