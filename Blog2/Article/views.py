from Article.models import *

from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.core.paginator import Paginator #django开发的分页模块

def index(request):
    return render_to_response("index.html")

def new_list(request,p=1):
    p = int(p)
    articles = Article.objects.order_by("-id")
    paginator = Paginator(articles,6) #将分页的总数据和单页的条数放入分页的模块
        #paginator.count #总条数 19900
        #paginator.num_pages #总页数
        #paginator.page_range #页码列表
    page = paginator.page(p) #获取具体页的数据
        #page.has_next() 是否由下一页
        #page.has_previous 是否由上一页
        #page.has_other 是否还有数据
    #获取页码
    start = p-3
    end = p+2
    if start <= 0:
        start = 0
    page_range = paginator.page_range[start:end]
    print(page_range)
    return render_to_response("new_list.html",locals())

def new(request,id):
    id = int(id)
    article = Article.objects.get(id = id)
    return render_to_response("article.html",locals())

def hello(request):
    return render_to_response("hello.html")

# Create your views here.
def add_article(request):
    for i in range(100,200):
        article = Article()
        article.title = "title_%s"%i
        article.content = "%s content"%i
        article.description = "%s description"%i

        article.author = Author.objects.get(id=1)
        article.save()
        article.type.add(
            Type.objects.get(id = 1)
        )
        article.save()

    return HttpResponse("save success")