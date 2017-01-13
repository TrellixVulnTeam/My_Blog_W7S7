from django.shortcuts import render, get_object_or_404
from .models import structure,comment
from django.core.paginator import PageNotAnInteger, Paginator, EmptyPage
from .forms import comment



def index(request):
    posts = structure.object.all()
    object_list = structure.publish.all()
    paginator = Paginator(object_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    return render(request, 'list.html', {'page': page, 'posts': posts})




def post_detail(request, year, month, day, post):
    post = get_object_or_404(structure, slug=post, status='published',
                             publish_year=year, publish_month=month, publish_day=day)
    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        comment_form = commentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
        else:
            comment_form = CommentForm()



    return render(request, 'detail.html', {'comments': comments,'comment_form': comment_form,
                                           'post': post})

