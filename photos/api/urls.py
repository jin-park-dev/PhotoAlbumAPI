from django.urls import path
from django.conf.urls import url
from django.views.static import serve


from photos.apps import PhotosConfig

from .views import PhotoCreateView, PhotoRUDView

app_name = PhotosConfig.name

urlpatterns = [
    path('', PhotoCreateView.as_view(), name='photo-create'),
    path('<int:pk>', PhotoRUDView.as_view(), name='photo-rud'),
    path('<slug:title>', PhotoRUDView.as_view(), name='photo-img'),
    url(r'^photo/(?P<path>.*)$', serve, {'document_root': 'photo',})
    # re_path(r'^bio/(?P<username>\w+)/$', views.bio, name='bio'),
]
