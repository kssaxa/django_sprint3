from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.utils.timezone import now
from blog.models import Post, Category
from django.utils import timezone


def index(request):
    current_time = now()

    template_name = "blog/index.html"
    post_list = Post.objects.filter(
        pub_date__lte=current_time, is_published=True, category__is_published=True
    ).order_by("-pub_date")[:5]
    context = {
        "post_list": post_list,
    }
    return render(request, template_name, context)


def post_detail(request, id):
    current_time = now()
    template_name = "blog/detail.html"
    post = get_object_or_404(
        Post,
        id=id,
        pub_date__lte=current_time,
        is_published=True,
        category__is_published=True
    )
    context = {"post": post}
    return render(request, template_name, context)


def category_posts(request, category_slug):
    current_time = now()
    template_name = "blog/category.html"
    category = get_object_or_404(
        Category,
        slug=category_slug,
        is_published=True,
    )
    posts = Post.objects.filter(
        category=category, 
        is_published=True, 
        pub_date__lte=current_time
    )
    context = {
        "category": category,
        "post_list": posts,
    }

    return render(request, template_name, context)
