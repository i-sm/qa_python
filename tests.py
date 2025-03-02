import pytest

from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        collector = BooksCollector()
        collector.add_new_book('Гордость и предубеждение и зомби')
        collector.add_new_book('Что делать, если ваш кот хочет вас убить')
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book_name', [
        'Съешь же ещё этих мягких французских бул',
        'Съешь же ещё этих мягких французских бу'
    ])
    def test_add_new_book_40_or_less_symbol_correct_adding(self, book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name in collector.books_genre

    def test_add_new_book_41_symbol_not_added(self):
        book_name = 'Съешь же ещё этих мягких французских було'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert book_name not in collector.books_genre

    def test_set_genre_added(self):
        book_name = 'Букварь'
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, "Фантастика")
        collector.get_book_genre(book_name)
        assert "Фантастика" == collector.get_book_genre(book_name)

    def test_get_book_genre_return_correct(self):
        book_name_1 = 'Букварь'
        collector_1 = BooksCollector()
        collector_1.add_new_book(book_name_1)
        collector_1.set_book_genre(book_name_1, "Фантастика")

        book_name_2 = 'Азбука'
        collector_2 = BooksCollector()
        collector_2.add_new_book(book_name_2)
        collector_2.set_book_genre(book_name_2, "Ужасы")
        assert "Ужасы" == collector_2.get_book_genre(book_name_2)

    def test_get_books_with_specific_genre_books_return_genres(self):
        book_name_3 = 'Словарь'
        collector_3 = BooksCollector()
        collector_3.add_new_book(book_name_3)
        collector_3.set_book_genre(book_name_3, "Ужасы")
        assert book_name_3 in collector_3.get_books_with_specific_genre("Ужасы")

    @pytest.mark.parametrize('book_name, genre', [
        ['Код в сапогах', 'Комедии'],
        ['Винни Пуз', 'Мультфильмы']
    ])
    def test_get_books_for_children_attribute_book_name_added(self, book_name, genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert book_name in collector.get_books_for_children()

    def test_add_book_in_favorites_book_once(self):
        collector = BooksCollector()
        collector.add_new_book("Синяя борода")
        collector.set_book_genre("Синяя борода", 'Ужасы')
        collector.add_book_in_favorites("Синяя борода")
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_get_list_of_favorites_books_correct(self):
        collector = BooksCollector()
        collector.add_new_book("Синяя борода")
        collector.set_book_genre("Синяя борода", 'Ужасы')
        collector.add_book_in_favorites("Синяя борода")
        assert "Синяя борода" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_book_true(self):
        collector = BooksCollector()
        collector.add_new_book("Синяя борода")
        collector.set_book_genre("Синяя борода", 'Ужасы')
        collector.add_book_in_favorites("Синяя борода")
        collector.delete_book_from_favorites("Синяя борода")
        assert "Синяя борода" not in collector.get_list_of_favorites_books()
