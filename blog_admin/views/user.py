from django.shortcuts import render,reverse,redirect
from common.models import *

def userlist(request):
    user = User.objects.all()
    context ={'userlist':user}
    return render(request,'admin/userlist.html',context)


def adduser(request):
    return render(request,'admin/adduser.html')


def insertuser(request):
    user = User()
    user.username = request.POST['username']

    import hashlib
    m = hashlib.md5()
    m.update(bytes(request.POST['password'], encoding='utf8'))
    user.password = m.hexdigest()

    user.email =request.POST['email']
    user.tel = request.POST['tel']
    user.save()
    return redirect(reverse(userlist))

def updateuser(request,uid):
    user = User.objects.get(id=uid)
    context ={'userlist':user}
    return render(request,'admin/edituser.html',context)


def edituser(request,uid):
    user = User.objects.get(id=uid)
    user.username = request.POST['username']
    import hashlib
    m = hashlib.md5()
    m.update(bytes(request.POST['password'], encoding='utf8'))
    user.password = m.hexdigest()

    user.email = request.POST['email']
    user.tel = request.POST['tel']
    user.save()
    return redirect(reverse(userlist))

def deleteuser(request,uid):
    user = User.objects.get(id=uid)
    user.delete()
    return redirect(reverse(userlist))
