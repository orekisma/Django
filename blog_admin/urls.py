from django.contrib import admin
from django.conf.urls import  url,include
from django.urls import path
from blog_admin.views import login,blog,uploads
from blog_admin.views import user

urlpatterns = [
    url(r'^$',login.login,name='login' ),
    url(r'^dologin$',login.dologin,name='dologin' ),
    url(r'^loginout$',login.loginout,name='loginout' ),

    url(r'^blog_index$',blog.blog_index,name='blog_index' ),
    url(r'^add_blog$',blog.add_blog,name='add_blog'),
    url(r'^insert_blog$',blog.insert_blog,name='insert_blog'),
    url(r'^update_blog/(?P<uid>[0-9]+)$',blog.update_blog,name='update_blog'),
    url(r'^edit_blog/(?P<uid>[0-9]+)$',blog.edit_blog,name='edit_blog'),
    url(r'^delete_blog/(?P<uid>[0-9]+)$',blog.delete_blog,name='delete_blog'),

    url(r'^upload/(?P<dir_name>[^/]+)$', uploads.upload_image, name='upload_image'),

    url(r'^userlist$',user.userlist,name='userlist' ),
    url(r'^adduser$',user.adduser,name='adduser' ),
    url(r'^insertuser$',user.insertuser,name='insertuser' ),
    url(r'^updateuser/(?P<uid>[0-9]+)$',user.updateuser,name='updateuser' ),
    url(r'^edituser/(?P<uid>[0-9]+)$',user.edituser,name='edituser' ),
    url(r'^deleteuser/(?P<uid>[0-9]+)$',user.deleteuser,name='deleteuser' ),


]
