from django.test import TestCase
from .models import Board
# Create your tests here.

class BoardTest:

    def setUpTestData(cls):
        Board.objects.create(title="board3")
        Board.objects.create(Description="this is board 3")

    def test_title_content(TestCase):
        Board = Board.objects.get(id=3)
        expected_object_name = f'{Board.title}'
        self.assertEquals(expected_object_name, 'board3')
