from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from photos.models import Photo, Album

# Like how form works
# 1. Serializers Converts to JSON
# 2. Validations for data passed


class PhotoRUDSerializer(serializers.ModelSerializer): # forms.ModelForm
    class Meta:
        model = Photo
        fields = [
            'pk',
            'name',
            'image',
            'viewed',
            'liked',
            'timestamp',
            'updated',
        ]
        read_only_fields = [
            'pk',
            'image',
        ]


class PhotoCreateSerializer(serializers.ModelSerializer):

    # image = Base64ImageField()

    class Meta:
        model = Photo
        fields = [
            'pk',
            'name',
            'image',
            'albums',
            'timestamp',
            'updated',
        ]


class AlbumRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Album
        fields = [
            'pk',
            'name',
            'description',
        ]
        read_only_fields = [
            'pk',
        ]


class AlbumCreateSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField()

    class Meta:
        model = Album
        fields = [
            'pk',
            'name',
            'description',
            'image',
        ]

    def get_image(self, obj):
        # Lets make it simple by getting first img. Later need algorithm to workout best img to return.
        # print(self)
        # print(type(obj))
        # print(obj)

        # request = self.context.get('request')
        # print(request.build_absolute_uri(obj.photo_set.first().image.url))

        image = "http://127.0.0.1:8000/api/photo/" + obj.photo_set.first().image.url
        return image