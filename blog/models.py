from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField('分类', max_length=128)

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = '博客分类'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    name = models.CharField('标签', max_length=128)

    def __str__(self):
        return self.name

    class Mate:
        verbose_name = '博客标签'
        verbose_name_plural = verbose_name


class Article(models.Model):
    title = models.CharField('标题', max_length=70)
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    created_time = models.DateTimeField('创建时间', auto_now_add=True)
    modifyed_time = models.DateTimeField('修改时间', auto_now=True)
    excerpt = models.TextField('摘要', max_length=200, blank=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, verbose_name='分类', blank=True, null=True)
    tags = models.ManyToManyField(Tag, verbose_name='标签', blank=True)
    views = models.PositiveIntegerField('阅读量', default=0)
    img = models.ImageField(upload_to='article_img/%Y/%m/%d', verbose_name='文章图片', blank=True)
    body = models.TextField('正文')

    def __str__(self):
        return self.title

    class Mate:
        verbose_name = '文章'
        verbose_name_plural = verbose_name

