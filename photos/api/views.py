from rest_framework import generics, mixins

from photos.models import Photo, Album
from .serializers import PhotoRUDSerializer, PhotoCreateSerializer


class PhotoCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    queryset = Photo.objects.all()
    serializer_class = PhotoCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PhotoRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Photo.objects.all()
    serializer_class = PhotoRUDSerializer
