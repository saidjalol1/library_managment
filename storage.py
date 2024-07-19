import json
import os
from book import Book

def load_books(file_path: str) -> dict:
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as file:
            books = json.load(file)
            return {int(k): Book(**v) for k, v in books.items()}
    return {}

def save_books(file_path: str, books: dict):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump({k: v.__dict__ for k, v in books.items()}, file, ensure_ascii=False, indent=4)
