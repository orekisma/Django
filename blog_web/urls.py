from blog_web.views import *
from blog_web import uploads
from django.conf.urls import  url,include


urlpatterns = [
    url(r'^(?P<pIndex>[0-9]*)$',web_index,name="web_index" ),
    url(r'^web_blog/(?P<uid>[0-9]+)$',web_blog,name="web_blog" ),
    url(r'^upload/(?P<dir_name>[^/]+)$',uploads.upload_image, name='upload_image'),

    url(r'^about',web_about,name="web_about"),
]
