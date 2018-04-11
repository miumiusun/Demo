from math import ceil

from django.shortcuts import render, redirect

from post.models import Post


def post_list(request):
    # posts = Post.objects.all()
    page = int(request.GET.get('page', 0)) or 1  # 当前页数
    total = Post.objects.count()              # 文章总数
    pages = ceil(total / 10)                  # 总页数

    start = (page - 1) * 10
    end = start + 10
    posts = Post.objects.all().order_by('-create')[start:end]

    return render(request, 'post_list.html', {'posts': posts, 'pages': range(1, pages + 1)})


def create(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        post = Post.objects.create(title=title, content=content)
        return redirect('/post/read/?post_id=%s' % post.id)

    return render(request, 'create.html')


def read(request):
    post_id = int(request.GET.get('post_id'))
    post = Post.objects.get(id=post_id)
    return render(request, 'read.html', {'post': post})


def edit(request):
    if request.method == 'POST':
        post_id = int(request.POST.get('post_id'))
        post = Post.objects.get(id=post_id)

        post.title = request.POST.get('title', '')
        post.content = request.POST.get('content', '')
        post.save()
        return redirect('/post/read/?post_id=%s' % post.id)
    else:
        post_id = int(request.GET.get('post_id'))
        post = Post.objects.get(id=post_id)
        return render(request, 'edit.html', {'post': post})


def search(request):
    keyword = request.POST.get('keyword', '')
    posts = Post.objects.filter(content__contains=keyword)
    return render(request, 'search.html', {'posts': posts})
