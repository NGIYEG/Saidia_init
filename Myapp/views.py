from django.shortcuts import render, redirect
import requests, base64
from requests.auth import HTTPBasicAuth
import json

from django.contrib import messages
from .models import Contact
from .forms import ContactForm ,SupporterForm


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')


def programmes(request):
    return render(request, 'program.html')

def support(request):
    if request.method == 'POST':
        form = SupporterForm(request.POST)
        if form.is_valid():
            form.save()
            # This message will now appear on the index page
            messages.success(request, 'Thank you! Your partnership request has been submitted.')
            
            # CHANGE THIS LINE:
            return redirect('home') 
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = SupporterForm()
    
    return render(request, 'support.html', {'form': form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you! Your message has been sent successfully.')
            return redirect('contact')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Blogpost
from .forms import BlogpostForm



def create_blogpost(request):
    if request.method == 'POST':
        form = BlogpostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post created successfully!')
            return redirect('blog_list')  # or wherever you want to redirect
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogpostForm()
    
    return render(request, 'create_blog.html', {'form': form})


def blog_list(request):
    blogposts = Blogpost.objects.all().order_by('-date_posted')
    return render(request, 'blog.html', {'blogposts': blogposts})


def blog_detail(request, pk):
    blogpost = Blogpost.objects.get(pk=pk)
    return render(request, 'blog_detail.html', {'blogpost': blogpost})


def update_blogpost(request, pk):
    blogpost = Blogpost.objects.get(pk=pk)
    if request.method == 'POST':
        form = BlogpostForm(request.POST, request.FILES, instance=blogpost)
        if form.is_valid():
            form.save()
            messages.success(request, 'Blog post updated successfully!')
            return redirect('blog_detail', pk=blogpost.pk)
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = BlogpostForm(instance=blogpost)
    
    return render(request, 'update_blog.html', {'form': form, 'blogpost': blogpost})


def delete_blogpost(request, pk):
    blogpost = Blogpost.objects.get(pk=pk)
    if request.method == 'POST':
        blogpost.delete()
        messages.success(request, 'Blog post deleted successfully!')
        return redirect('blog_list')
    
    return render(request, 'delete_blog.html', {'blogpost': blogpost})