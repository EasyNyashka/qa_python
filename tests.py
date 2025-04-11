import pytest
class TestBooksCollector:
# Tесты на первый метод
    @pytest.mark.parametrize('book_name', ['Я','Домовенок Кузя', 'В названии книги ровно сорок символов 40'])
    def test_add_new_book_add_one_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name', ['В названии книги ровно сорок один символ ', 'Очень длинное название книги, очень-очень-очень', ''])
    def test_add_new_book_invalid_name_book(self, collector, book_name):
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    def test_add_new_book_add_the_same_book(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.add_new_book('Домовенок Кузя')
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

# Тесты на 4 метод
    def test_get_books_with_specific_genre_valid_gerne(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.add_new_book('Золушка')
        collector.add_new_book('Оно')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Домовенок Кузя', 'Мультфильмы')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        assert collector.get_books_with_specific_genre('Мультфильмы') == ['Домовенок Кузя', 'Золушка']
        assert collector.get_books_with_specific_genre('Мультфильмы') != ['Оно']

    def test_get_books_with_specific_genre_invalid_gerne(self, collector):
        assert collector.get_books_with_specific_genre('Советские мультфильмы') == []

# Тесты на 5 метод
    def test_get_books_genre_not_an_empty_dictionary(self, collector):
        collector.add_new_book('Золушка')
        collector.add_new_book('Оно')
        collector.set_book_genre('Золушка', 'Мультфильмы')
        collector.set_book_genre('Оно', '')
        assert collector.get_books_genre() == {'Золушка': 'Мультфильмы', 'Оно':''}

    def test_get_books_genre_empty_dictionary(self, collector):
        assert collector.get_books_genre() == {}

# Тесты на 6 метод
    def test_get_books_for_children_no_adult_books(self, collector):
        collector.add_new_book('Затерянный мир')
        collector.add_new_book('Домовенок Кузя')
        collector.set_book_genre('Затерянный мир', 'Фантастика')
        collector.set_book_genre('Домовенок Кузя', 'Мультфильмы')
        assert collector.get_books_for_children() == ['Затерянный мир', 'Домовенок Кузя']

    def test_get_books_for_children_with_adult_books(self, collector):
        collector.add_new_book('Оно')
        collector.add_new_book('Домовенок Кузя')
        collector.set_book_genre('Оно', 'Ужасы')
        collector.set_book_genre('Азазель', 'Детектив')
        assert collector.get_books_for_children() == []

# Тесты на 7 метод
    def test_add_book_in_favorites_valid(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.add_book_in_favorites('Домовенок Кузя')
        assert collector.get_list_of_favorites_books() == ['Домовенок Кузя']

    def test_add_book_in_favorites_no_book(self, collector):
        collector.add_book_in_favorites('Домовенок Кузя')
        assert collector.get_list_of_favorites_books() == []

    def test_add_book_in_favorites_valid(self, collector):
        collector.add_new_book('Домовенок Кузя')
        collector.add_book_in_favorites('Домовенок Кузя')
        collector.add_book_in_favorites('Домовенок Кузя')
        assert len(collector.get_list_of_favorites_books()) == 1






