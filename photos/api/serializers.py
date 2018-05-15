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

