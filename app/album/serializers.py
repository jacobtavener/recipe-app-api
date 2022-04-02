from rest_framework import serializers

from core.models import Tag, Artist


class TagSerializer(serializers.ModelSerializer):
    """Serializer for tag object"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)


class ArtistSerializer(serializers.ModelSerializer):
    """Serializer for artist object"""

    class Meta:
        model = Artist
        fields = ('id', 'name')
        read_only_fields = ('id',)
