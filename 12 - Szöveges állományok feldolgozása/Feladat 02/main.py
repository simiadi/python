from book import Book
from typing import *
from bookIO import *
from services import *

filename: str = "data/adatok.txt"
books: List[Book] = readBooksFromFile(filename)

writeToConsole(books)

booksByTheme: List[Book] = getBooksByTheme("informatika", books)

writeBooksInFile(booksByTheme, "informatika")

booksFromPublishInterval: List[Book] = getBooksByPublishYearInterval(1900, 1999, books)

writeBooksInFile(booksFromPublishInterval, "1900")