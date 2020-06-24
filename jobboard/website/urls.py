"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('blog.html',views.blog,name="blog"),
    path('blog_single.html',views.blog_single,name="blog_single"),
    path('browsejobs.html',views.browsejobs,name="browsejobs"),
    path('candidates.html',views.candidates,name="candidates"),
    path('contact.html',views.contact,name="contact"),
    path('job_post.html',views.job_post,name="job_post"),
    path('new_post.html',views.new_post,name="new_post"),
]