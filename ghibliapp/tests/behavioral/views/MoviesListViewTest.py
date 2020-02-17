from django.urls import reverse
from django.test import TestCase
from ghibliapp.models import Movie, Person


class MoviesListViewTest(TestCase):
    def test_empty_movies(self):
        response = self.client.get('/movies')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'No Movie lists available at the time. Have you updated the data from ghibli?')
        self.assertQuerysetEqual(response.context['movie_list'], [])

    def test_one_movie_no_people(self):
        Movie.objects.create(
            externalId='570c3a56-059e-4ce8-aac6-c504e5bf3a48',
            title='title',
            description='description'
        )

        response = self.client.get('/movies')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        self.assertQuerysetEqual(
            response.context['movie_list'],
            ["{'movie': <Movie: Movie object (570c3a56-059e-4ce8-aac6-c504e5bf3a48)>, ""'people': <QuerySet []>}"]
        )

    def test_one_movie_multiple_people(self):
        movie = Movie.objects.create(
            externalId='570c3a56-059e-4ce8-aac6-c504e5bf3a48',
            title='test',
            description='test_description'
        )

        person1 = Person.objects.create(
            externalId='16156619-5182-4291-be19-af46829f8218',
            name='person1'
        )

        person2 = Person.objects.create(
            externalId='f981c8d2-d146-43e2-9f4a-1b7b6dd5ef7e',
            name='person2'
        )
        movie.person_set.add(person1, person2)

        response = self.client.get('/movies')

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'title')
        self.assertContains(response, 'description')
        self.assertContains(response, 'person1')
        self.assertContains(response, 'person2')
        self.assertQuerysetEqual(
            response.context['movie_list'],
            ["{'movie': <Movie: Movie object (570c3a56-059e-4ce8-aac6-c504e5bf3a48)>, "
             "'people': <QuerySet [<Person: Person object "
             '(16156619-5182-4291-be19-af46829f8218)>, <Person: Person object '
             '(f981c8d2-d146-43e2-9f4a-1b7b6dd5ef7e)>]>}']
        )
