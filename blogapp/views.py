from django.shortcuts import redirect, render
from .models import (
    Post,
    Category1,
    Category2,
    Comment,
    Cardio_Video,
    Strength_Video,
    Power_Video,
    Flex_Video,
)
from django.contrib import messages
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
)

from .models import Post

# Create your views here.
class BlogTemplateView(TemplateView):
    model = Post
    template_name = "blogapp/about.html"


class BlogListView(ListView):
    model = Post
    template_name = "blogapp/categories.html"


class BlogListView(ListView):
    model = Post
    template_name = "blogapp/learn.html"


class BlogListView(ListView):
    model = Post
    template_name = "blogapp/exercise/cardio.html"


class BlogListView(ListView):
    model = Post
    template_name = "blogapp/exercise/strength.html"


class BlogListView(ListView):
    model = Post
    template_name = "blogapp/exercise/power.html"


class BlogListView(ListView):
    model = Post
    template_name = "blogapp/exercise/flex.html"


class PostDetailView(DetailView):
    model = Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ["title", "slug", "body", "image", "first_category", "second_category"]
    template_name = "blogapp/edit/post_form.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ["title", "slug", "body", "image", "first_category", "second_category"]
    template_name = "blogapp/edit/post_detail.html"
    success_url = "/"

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = "blogapp/edit/post_delete.html"
    success_url = "/"

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


def HomePage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
    }
    return render(request, "blogapp/index.html", context)


def ArticleDetail(request, slug):
    get_post = Post.objects.get(slug=slug)
    get_all_comments = Comment.objects.filter(post_name=get_post)

    number_of_comments = 0
    for i in get_all_comments:
        number_of_comments += 1

    if request.method == "POST":
        name = request.POST["name"]
        body = request.POST["body"]

        new_comment = Comment(name=name, post_name=get_post, body=body)
        new_comment.save()

        messages.success(request, "Comment was added successfully!")
        return redirect("detail", slug=slug)

    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    get_all_posts = Post.objects.all()

    get_cat_1 = get_post.first_category
    get_cat_2 = get_post.second_category
    context = {
        "posts": get_all_posts,
        "post": get_post,
        "category1": get_cat_1,
        "category2": get_cat_2,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
        "comments": get_all_comments,
        "number_of_comments": number_of_comments,
    }
    return render(request, "blogapp/article.html", context)


def LearnPage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
    }
    return render(request, "blogapp/learn.html", context)


def AboutPage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
    }
    return render(request, "blogapp/about.html", context)


def CategoriesPage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
    }
    return render(request, "blogapp/categories.html", context)


def CardioPage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    videos = Cardio_Video.objects.all()
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
        "videos": videos,
    }
    return render(request, "blogapp/exercise/cardio.html", context)


def StrengthPage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    videos = Strength_Video.objects.all()
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
        "videos": videos,
    }
    return render(request, "blogapp/exercise/strength.html", context)


def PowerPage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    videos = Power_Video.objects.all()
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
        "videos": videos,
    }
    return render(request, "blogapp/exercise/power.html", context)


def FlexPage(request):
    get_all_posts = Post.objects.all()
    get_all_categories_in_category_1 = Category1.objects.all()[:2]
    get_all_categories_in_category_2 = Category2.objects.all()[:2]
    videos = Flex_Video.objects.all()
    context = {
        "posts": get_all_posts,
        "cat1": get_all_categories_in_category_1,
        "cat2": get_all_categories_in_category_2,
        "videos": videos,
    }
    return render(request, "blogapp/exercise/flex.html", context)


def blog_detail(request, pk):
    Tut = tutorial.objects.get(pk=pk)
    context = {
        "Tut": Tut,
    }
    return render(request, "blogdetail.html", context)
