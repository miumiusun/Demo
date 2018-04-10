from django.shortcuts import render, redirect

from post.models import Post


def post_list(request):
    data = {}
    return render(request, 'post_list.html', data)


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
    data = {}
    return render(request, 'edit.html', data)


def search(request):
    data = {}
    return render(request, 'search.html', data)
