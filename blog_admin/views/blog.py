from django.shortcuts import render
from django.shortcuts import reverse,redirect
from common.models import *
from blog_admin.views.login import *
from django.http import HttpResponse
import time, os


def blog_index(request):
    if request.session.get('user',None):
        blog = Blog.objects.all()
        context = {'list':blog}
        return render(request,'admin/index.html',context)
    else:
        return render(request, 'admin/login.html')

def add_blog(request):
    if request.session.get('user', None):
        return render(request,'admin/addblog.html')
    else:
        return render(request, 'admin/login.html')

def insert_blog(request):
    myfile = request.FILES.get('pic')
    print(myfile)
    if not myfile:
        return HttpResponse("没有上传文件信息")
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open("./static/pics/" + filename, "wb+")
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()


    blog = Blog()
    blog.title = request.POST['title']
    blog.tag = request.POST['tag']
    blog.guide = request.POST['guide']
    blog.content = request.POST['content']
    blog.filename = filename
    blog.save()
    return redirect(reverse(blog_index))


def update_blog(request,uid):
    if request.session.get('user', None):
        blog = Blog.objects.get(id=uid)
        context ={'list':blog}
        return render(request,'admin/edit.html',context)
    else:
        return render(request, 'admin/login.html')


def edit_blog(request,uid):
    myfile = request.FILES.get('pic')
    print(myfile)
    if myfile is None:
        return HttpResponse('无文件')
    print(myfile)
    filename = str(time.time()) + "." + myfile.name.split('.').pop()
    destination = open("./static/pics/" + filename, "wb+")
    for chunk in myfile.chunks():  # 分块写入文件
        destination.write(chunk)
    destination.close()

    blog = Blog.objects.get(id=uid)

    # 删除原图片
    img1 = "./static/pics/" + blog.filename
    if os.path.exists(img1):
        os.remove(img1)

    blog.title = request.POST['title']
    blog.tag = request.POST['tag']
    blog.guide = request.POST['guide']
    blog.content = request.POST['content']
    blog.filename = filename
    blog.save()

    return redirect(reverse(blog_index))


def delete_blog(request,uid):
    blog = Blog.objects.get(id=uid)
    img1 = "./static/pics/" + blog.filename
    if os.path.exists(img1):
        os.remove(img1)

    blog.delete()
    return redirect(reverse(blog_index))

