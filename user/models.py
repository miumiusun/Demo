from django.db import models


class User(models.Model):
    SEX = (
        ('M', '男'),
        ('F', '女'),
        ('U', '保密'),
    )
    nickname = models.CharField(max_length=32)   # 昵称
    password = models.CharField(max_length=128)  # 密码
    icon = models.ImageField()                   # 头像
    age = models.IntegerField()                  # 年龄
    sex = models.CharField(choices=SEX)          # 性别
