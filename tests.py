import pytest
class TestBooksCollector:
# Tесты на первый метод
    @pytest.mark.parametrize('book_name', ['Я','Гордость и предубеждение и зомби', 'В названии книги ровно сорок символов 40'])
    def test_add_new_book_add_one_books(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name', ['В названии книги ровно сорок один символ ', 'Очень длинное название книги, очень-очень-очень', ''])
    def test_add_new_book_invalid_name_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_the_same_book(self, collector):
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Гордость и предубеждение и зомби')
        assert len(collector.books_genre) == 1

# Тесты на второй метод
    def test_set_book_genre_valid(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.set_book_genre('Домовенок Кузя', 'Мультфильмы')
        assert collector.get_book_genre('Домовенок Кузя') == 'Мультфильмы'

    def test_set_book_genre_no_book(self, collector):
        collector.set_book_genre('Домовенок Кузя', 'Мультфильмы')
        assert 'Домовенок Кузя' not in collector.books_genre

    def test_set_book_genre_invalid_genre(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.set_book_genre('Домовенок Кузя', 'Советские мультфильмы')
        assert collector.get_book_genre('Домовенок Кузя') == ''

        # Тесты на 3 метод
    def test_get_book_genre_book_exists(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.set_book_genre('Домовенок Кузя', 'Мультфильмы')
        assert collector.get_book_genre('Домовенок Кузя') == 'Мультфильмы'

    def test_get_book_genre_invalid_genre_book(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.set_book_genre('Домовенок Кузя', 'Мультфильмы')
        assert collector.get_book_genre('Домовенок Кузя') != 'Детективы'

    def test_get_book_genre_book_nonexists(self, collector):
        assert collector.get_book_genre('Домовенок Кузя') is None


