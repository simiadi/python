from book import Book
from typing import *

def writeToConsole(books: List[Book]) -> None:
    for book in books:
        print(book)

def getBooksByTheme(theme: str, books: List[Book]) -> List[Book]:
    filteredBooks: List[Book] = []

    for book in books:
        if(book.theme == theme):
            filteredBooks.append(book)
    
    return filteredBooks

def getBooksByPublishYearInterval(startYear: int, endYear: int, books: List[Book]) -> List[Book]:
    filteredBooks: List[Book] = []

    for book in books:
        if(book.publishYear >= startYear and book.publishYear <= endYear):
            filteredBooks.append(book)
    
    return filteredBooks