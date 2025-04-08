import pytest
class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book_name', ['Очень длинное название книги, очень-очень-очень', ''])
    def test_add_new_book_invalid_name_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_the_same_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1



