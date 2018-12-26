# coding:utf8
from django.db import models
#每次修改好models后需要生成并执行迁移
# Create your models here.
class Gallery(models.Model):
    description = models.CharField(default='file_name',max_length=100)
    images = models.ImageField(default='default.png',upload_to='images/')
    title = models.CharField(default='file_name',max_length=50)
    #该函数用于改变表格栏的名称
    def __str__(self):
        return self.title
