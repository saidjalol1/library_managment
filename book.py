class Book:
    def __init__(self, book_id: int, title: str, author: str, year: int, status: str):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def __str__(self):
        return f'ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Year: {self.year}, Status: {self.status}'
