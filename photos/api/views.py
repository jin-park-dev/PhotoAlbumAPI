from rest_framework import generics, mixins

from photos.models import Photo, Album
from .serializers import PhotoRUDSerializer, PhotoCreateSerializer, AlbumCreateSerializer, AlbumRUDSerializer


class PhotoCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PhotoCreateSerializer

    def get_queryset(self):
        # print(self.request.__dict__)
        return Photo.objects.all()

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class PhotoRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Photo.objects.all()
    serializer_class = PhotoRUDSerializer


class AlbumCreateView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'pk'
    queryset = Album.objects.all()
    serializer_class = AlbumCreateSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get_serializer_context(self, *args, **kwargs):
    #     context = super(AlbumCreateView, self).get_serializer_context()
    #     context.update({
    #         "exclude_email_list": ['test@test.com', 'test1@test.com']
    #         # extra data
    #     })
    #     print(context)
    #     return context


class AlbumSingleView(generics.ListAPIView):
    lookup_field = 'pk'
    serializer_class = PhotoCreateSerializer

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        album = Album.objects.filter(pk=pk).first()
        photos = album.photo_set.all()
        # print(Photo.objects.all())
        # photo_set = album.photo_set.all()
        # print('photo_set')
        # print(photo_set)
        return photos

    # def get_serializer_context(self, *args, **kwargs):
    #     context = super(AlbumCreateView, self).get_serializer_context()
    #     context.update({
    #         "exclude_email_list": ['test@test.com', 'test1@test.com']
    #         # extra data
    #     })
    #     print(context)
    #     return context


class AlbumRUDView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = Album.objects.all()
    serializer_class = AlbumRUDSerializer


