import pytest

from main import BooksCollector


class TestBooksCollector:


    def test_add_new_book_add_two_books(collector):

      #  collector = BooksCollector()

        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')

        assert len(collector.books_genre) == 2

