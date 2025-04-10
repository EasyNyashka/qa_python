# qa_python

## sprint4

### Необходимо покрыть тестами приложение BooksCollector

- Создала окружение, добавила файл `cоnftest.py`, создала фикстуру на объект класса
- Для 1 метода `add_new_book` написала 3 позитивных теста с учетом граничных значений и 3 негативных на длину названия больше 40 символов и добавление одной и той же книги
- Для 2 метода `set_book_genre`: 1 позитивный на установку жанра книги, который есть в списке жанров,и 2 негативных: нельзя установить жанр на несуществующую книгу и установить несуществующий жанр
- Для 3 метода `get_book_genre` написала позитивный тест: выводит жанр книги по её имени, и два негативных теста: 1. не выводит жанр книги, несоответствующей этой книге, и 2. реакция на отсутсвие книги в списке
- Для 4 метода `get_books_with_specific_genre` написала тест проверяющй, что метод корректно фльтрует книги по жанру и возвращает пустой список, если такого жанра не существует
