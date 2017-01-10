from django.shortcuts import render, get_object_or_404
from .models import structure


def index(request):
    posts = structure.published.all()
    return render(request,'app/post/list.html',{'posts': posts})

def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'app/post/detail.html',{'post': post})