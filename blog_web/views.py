from django.shortcuts import render
from django.core.paginator import Paginator
from common.models import *
# Create your views here.



def web_index(request,pIndex):

    blog = Blog.objects.all()
    p = Paginator(blog,4)
    if pIndex=='':
        pIndex = 1
    pIndex = int(pIndex)
    list2 = p.page(pIndex)
    plist = p.page_range


    context ={'list':list2,'pIndex':pIndex,'plist':plist}
    return render(request,'web/index.html',context)



def web_blog(request,uid):

    blog =Blog.objects.get(id=uid)
    context ={'list':blog}
    return render(request,'web/details.html',context)


def web_about(requset):
    return render(requset,'web/about.html')
