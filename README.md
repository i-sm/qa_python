# qa_python

Добавлены тесты:

| Метод кода                      | Тест                                                     | Описание                                                  |
|---------------------------------|----------------------------------------------------------|-----------------------------------------------------------|
| add_new_book()                  | test_add_new_book_add_two_books()                        | Проверка, что две книги добавляются                       |
| add_new_book()                  | test_add_new_book_40_or_less_symbol_correct_adding       | Проверка добавления книги с корректным кол-вом символов   |
| add_new_book()                  | test_add_new_book_41_symbol_not_added()                  | Проверка добавления книги с некорректным кол-вом символов |
| set_book_genre                  | test_set_genre_added()                                   | Проверка добавления жанра                                 |
| get_book_genre()                | test_get_book_genre_return_correct()                     | Проверка возвращения жанра по названию книги              |
| get_books_with_specific_genre() | test_get_books_with_specific_genre_books_return_genres() | Получение всех книг по жанру                              |
| get_books_for_children()        | test_get_books_for_children_attribute_book_name_added()  | Проверка возврата детских книг                            |
| add_book_in_favorites()         | test_add_book_in_favorites_book_once()                   | Проверка добавления книги в избранное                     |
| delete_book_from_favorites()    | test_delete_book_from_favorites_book_true()              | Проверка удаления книги в избранное                       |
| get_list_of_favorites_books()   | test_get_list_of_favorites_books_correct()               | Проверка получения книги в избранное                      |
