from django.conf import settings
from django.urls import path
from django.conf.urls.static import static

from . import views

# app_name = "Saidia"
urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'), 
     path('about/', views.about, name='about'),
     path('contact/', views.contact, name='contact'),
     path('programmes/', views.programmes, name='programmes'),
     path('support/', views.support, name='support'),
     path('blog/', views.blog_list, name='blog'),
    path('blog/create/', views.create_blogpost, name='create_blog'),
    path('blog/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('blog/<int:pk>/edit/', views.update_blogpost, name='update_blog'),
    path('blog/<int:pk>/delete/', views.delete_blogpost, name='delete_blog'),
     
]
