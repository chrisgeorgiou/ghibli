from rest_framework import serializers
from ghibliapp.models import Person, Movie
from ghibliapp.extractor import ExtractFilmIds


class PersonSerializer(serializers.ModelSerializer):
    id = serializers.CharField(source='externalId')
    films = serializers.ListField(child=serializers.CharField())

    class Meta:
        model = Person
        fields = ['id', 'name', 'films']

    def create(self, validated_data):
        person = Person()
        person.externalId = validated_data['externalId']
        person.name = validated_data['name']
        person.save()

        for url in validated_data['films']:
            movie_id = ExtractFilmIds(url).export_film_uuid()
            person.movies.add(Movie.objects.get(externalId=movie_id))

        return person
