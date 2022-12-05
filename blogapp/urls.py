from django.urls import path
from blogapp import views
from .import  views
from django.views.generic import TemplateView
from .views import (
    BlogListView,
    BlogTemplateView,
    PostDetailView,
    PostUpdateView,
    PostDeleteView,
    PostCreateView
    
)

urlpatterns = [
    path('', views.HomePage, name='home'),
    path('blog-detail/<str:slug>/', views.ArticleDetail, name='detail'),
    path("home/categories/", views.CategoriesPage, name="categories"),
    path('home/about', views.AboutPage, name="about"),
    path("exercise/cardio/", views.CardioPage, name="cardio"),
    path("exercise/strength/", views.StrengthPage, name="strength"),
    path("exercise/power/", views.PowerPage, name="power"),
    path("exercise/flex/", views.FlexPage, name="flex"),
    path("home/learn", views.LearnPage, name="learn"),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    
]
#BlogTemplateView.as_view()