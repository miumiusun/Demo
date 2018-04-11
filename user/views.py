from django.shortcuts import render


def register(request):
    if request.method == 'POST':
        # 获取 POST 数据
        # 验证数据有效性 -> 可以使用表单验证
            # 验证密码
        # 保存头像
        # 创建用户
        # session 写入登陆状态
        # 返回用户信息页

    return render(request, 'register.html', {})


def login(request):
    if request.method == 'POST':
        # 取出 POST 数据
        # 验证密码
        # session 写入登陆状态
        # 跳转到 用户信息页
    return render(request, 'login.html', {})


def user_info(request):
    return render(request, 'user_info.html', {})


def logout(request):
    # 删除用户的 session 数据
    return render(request, 'logout.html', {})
