
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Category,User
from django.utils import timezone
from django.views.generic import (ListView,
                                DetailView,
                                UpdateView,
                                CreateView,
                                DeleteView)
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib import messages


class BlogLoginView(LoginView):
    redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('post_list') 
    
    def form_invalid(self, form):
        messages.error(self.request,'Invalid username or password')
        return self.render_to_response(self.get_context_data(form=form))


class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'


class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'


class PostUpdateView(UpdateView):
    model = Post
    fields = ["title", 'text']
    template_name = 'blog/post_edit.html'

    def get_queryset(self):
        return Post.objects.filter(author=self.request.user)



class PostCreateView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'login'
    model = Post
    fields = ["title",'text']
    template_name = 'blog/post_create.html'

    def form_valid(self, form):
        fields = form.save(commit=False)
        fields.author = self.request.user
     
        fields.save()
        return super().form_valid(form)
    
class PostDeleteView(DeleteView):
    model = Post
    success_url = '/'
    template_name = 'blog/post_delete.html'

        
# def post_list(request):
#     posts = Post.objects.all()
#     return render(request, 'blog/post_list.html', {'posts':posts})


# def post_detail(request, pk):
#     post = get_object_or_404(Post, pk=pk)
#     return render(request, 'blog/post_detail.html', {'post':post})



# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST)
#         if form.is_valid():
#             post = form.save(commit=False)
#             post.author = request.user
#             post.pub_date = timezone.now()
#             post.save()
#             return redirect('post_detail', pk=post.pk)
#     else:
#         form = PostForm()
#         return render(request, 'blog/post_create.html', {'form': form})
    



# def post_edit(request, pk):
#     post = get_object_or_404(Post, pk=pk)

#     if request.method == 'POST':
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#             return redirect('post_detail', pk=post.pk) 
#     else:
#         form = PostForm(instance=post)

#     return render(request, 'blog/post_edit.html', {'form': form})


def category_list(request):
    categories = Category.object.all()
    return render(request, 'blog/cat_list.html', {'categories':categories})