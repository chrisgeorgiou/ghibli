import urllib3
import json

from django.core.management.base import BaseCommand, CommandError
from ghibliapp.serializers import MovieSerializer, PersonSerializer
from django.conf import settings


class Command(BaseCommand):
    help = 'Retrieves the data from Ghibli and stores them in database'
    http = urllib3.PoolManager()

    def handle(self, *args, **options):

        # Unfortunately the Ghibli API doesn't allow as to know if there is
        # paginated data in the response so we can only retrieve the 250
        # maximum data from the API. This needs to be updated in the way we
        # can loop through the pages.

        # load all the films from the API, deserialize them to our model
        # and persist it
        requestFilms = self.http.request(
            'GET',
            settings.GHIBLI_BASE_PATH + 'films?limit=250'
        )
        parsed_response = json.loads(requestFilms.data)

        movieDeserialize = MovieSerializer(data=parsed_response, many=True)
        movieDeserialize.is_valid(raise_exception=True)
        movieDeserialize.save()

        requestPeople = self.http.request(
            'GET',
            settings.GHIBLI_BASE_PATH + 'people?limit=250'
        )
        parsed_response = json.loads(requestPeople.data)

        personDeserialize = PersonSerializer(data=parsed_response, many=True)
        personDeserialize.is_valid(raise_exception=True)
        personDeserialize.save()

        self.stdout.write(
            self.style.SUCCESS('Successfully persisted all films and people')
        )
