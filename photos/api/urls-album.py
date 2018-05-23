from django.urls import path, re_path
from django.views.static import serve


from photos.apps import PhotosConfig

from .views import AlbumCreateView, AlbumSingleView

app_name = PhotosConfig.name

urlpatterns = [
    path('', AlbumCreateView.as_view(), name='album-create'),
    path('<int:pk>', AlbumSingleView.as_view(), name='album-single'),

    re_path(r'^photo/(?P<path>.*)$', serve, {'document_root': 'photo'}),
]
