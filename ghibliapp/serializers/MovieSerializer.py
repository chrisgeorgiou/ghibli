from rest_framework import serializers
from ghibliapp.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='externalId')

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description']

    def create(self, validated_data):
        movie = Movie()
        movie.externalId = validated_data['externalId']
        movie.title = validated_data['title']
        movie.description = validated_data['description']
        movie.save()

        return movie
