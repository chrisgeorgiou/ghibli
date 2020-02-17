from ghibliapp.extractor import ExtractFilmIds

from unittest import TestCase
from parameterized import parameterized


class ExtractFilmIdsTest(TestCase):
    @parameterized.expand([
        ('http://something/films/d7015d60-9a27-4a25-9594-b5132e8ca190', 'd7015d60-9a27-4a25-9594-b5132e8ca190',),
        ('http://something/films/240bc9f5-381a-4bd4-9dc2-4bf76f78142a', '240bc9f5-381a-4bd4-9dc2-4bf76f78142a',),
        ('http://something/films/6219bf59-79c9-41bf-ac08-0b10defb25b8', '6219bf59-79c9-41bf-ac08-0b10defb25b8',),
        ('http://something/films/9d195a63-940a-4bc3-ad41-8a3e6b67f3ce', '9d195a63-940a-4bc3-ad41-8a3e6b67f3ce',),
        ('http://something/films/fa4633c3-8077-44e2-87db-a3162a97a751', 'fa4633c3-8077-44e2-87db-a3162a97a751',),
    ])
    def test_extraction_with_correct_values(self, given_value, expected_value):
        extractor = ExtractFilmIds(given_value)
        self.assertEqual(extractor.export_film_uuid(), expected_value)

    @parameterized.expand([
        ('http://something/people/d7015d60-9a27-4a25-9594-b5132e8ca190', '',),
        ('http://something/films/stringsomething', '',),
        ('http://something/film/6219bf59-79c9-41bf-ac08-0b10defb25b8', '',),
        ('http://something/films/1', '',),
        ('http://something/films/?filters', '',),
    ])
    def test_extraction_with_wrong_values(self, given_value, expected_value):
        extractor = ExtractFilmIds(given_value)
        self.assertEqual(extractor.export_film_uuid(), expected_value)
