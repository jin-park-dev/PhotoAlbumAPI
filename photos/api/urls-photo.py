from django.urls import path, re_path
from django.views.static import serve


from photos.apps import PhotosConfig

from .views import PhotoCreateView, PhotoRUDView

app_name = PhotosConfig.name

urlpatterns = [
    path('', PhotoCreateView.as_view(), name='photo-create'),
    path('<int:pk>', PhotoRUDView.as_view(), name='photo-rud'),
    path('<slug:title>', PhotoRUDView.as_view(), name='photo-img'),
    re_path(r'^photo/(?P<path>.*)$', serve, {'document_root': 'photo'}), # Need to look. URL doesn't seem to do anything here.
]
