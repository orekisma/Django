from django.shortcuts import render
from django.shortcuts import reverse,redirect
from blog_admin.views.blog import *
from common.models import *
import hashlib


def login(request):
    return render(request, 'admin/login.html')



def dologin(request):
    user = User.objects.get(username=request.POST['username'])
    m = hashlib.md5()
    m.update(bytes(request.POST['password'], encoding="utf8"))
    if user.password == m.hexdigest():
        request.session['user'] = user.username
        return redirect(reverse(blog_index))
    else:
        return render(request, 'admin/login.html')



def loginout(request):
    del request.session['user']
    return redirect(reverse(login))