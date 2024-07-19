import json
import os
from book import Book
from storage import load_books, save_books

class Library:
    def __init__(self, storage_file: str):
        self.storage_file = storage_file
        self.books = load_books(storage_file)

    def add_book(self, title: str, author: str, year: int):
        book_id = max(self.books.keys(), default=0) + 1
        book = Book(book_id, title, author, year, 'в наличии')
        self.books[book_id] = book
        save_books(self.storage_file, self.books)
        print(f'Книга "{title}" добавлена с id {book_id}')

    def remove_book(self, book_id: int):
        if book_id in self.books:
            del self.books[book_id]
            save_books(self.storage_file, self.books)
            print(f'Книга с id {book_id} удалена')
        else:
            print(f'Книга с id {book_id} не найдена')

    def find_books(self, search_term: str):
        results = [book for book in self.books.values() if search_term.lower() in book.title.lower() or
                   search_term.lower() in book.author.lower() or search_term == str(book.year)]
        if results:
            for book in results:
                print(book)
        else:
            print('Книги не найдены')

    def display_books(self):
        if self.books:
            for book in self.books.values():
                print(book)
        else:
            print('Библиотека пуста')

    def update_status(self, book_id: int, status: str):
        if book_id in self.books:
            if status in ['в наличии', 'выдана']:
                self.books[book_id].status = status
                save_books(self.storage_file, self.books)
                print(f'Статус книги с id {book_id} обновлен на "{status}"')
            else:
                print('Некорректный статус')
        else:
            print(f'Книга с id {book_id} не найдена')

def main():
    library = Library('library.json')

    while True:
        print("\n1. Добавить книгу\n2. Удалить книгу\n3. Найти книгу\n4. Показать все книги\n5. Изменить статус книги\n6. Выход")
        choice = input("Выберите действие: ")
        
        if choice == '1':
            title = input("Введите название книги: ")
            author = input("Введите автора книги: ")
            year = int(input("Введите год издания: "))
            library.add_book(title, author, year)
        elif choice == '2':
            book_id = int(input("Введите id книги для удаления: "))
            library.remove_book(book_id)
        elif choice == '3':
            search_term = input("Введите название, автора или год издания для поиска: ")
            library.find_books(search_term)
        elif choice == '4':
            library.display_books()
        elif choice == '5':
            book_id = int(input("Введите id книги для изменения статуса: "))
            status = input("Введите новый статус (в наличии/выдана): ")
            library.update_status(book_id, status)
        elif choice == '6':
            break
        else:
            print("Неверный выбор, попробуйте снова.")

if __name__ == "__main__":
    main()
