import unittest
import functions


class MyFirstTest(unittest.TestCase):
    def test_favorite_movie(self):
        rez = "forsage"
        self.assertEqual(functions.favorite_movie(rez), "my favorite movie is forsage")

    def test_make_country(self):
        country = "Ukraine"
        capital = "Kyiv"
        rez = {"Ukraine": "Kyiv"}
        self.assertEqual(functions.make_country(country, capital), rez)

    def test_make_operation(self):
        rez = (48, 1)
        self.assertEqual(functions.make_operation("+", 3, 4, 8, 33), rez)
