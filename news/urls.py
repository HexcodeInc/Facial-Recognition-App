from django.conf.urls import url
from . import views

urlpatterns = [url(r'index',views.index,name = 'index'),
url(r'game/(?P<value>[0-9]+)',views.games,name = 'game'),
url(r'politics/(?P<value>[a-z]+)/(?P<value2>[0-9]+)',views.politics,name = 'politics'),
url(r'camera/',views.camera,name ='camera'),
url(r'classify/upload',views.upload,name = 'imageupload'),
]