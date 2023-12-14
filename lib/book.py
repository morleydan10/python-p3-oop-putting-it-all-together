#!/usr/bin/env python3

class Book:

    def __init__(self, title = '', page_count = 0):
        self.title = title
        self.page_count = page_count

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, title):
        if isinstance(title, str):
            self._title = title
            print(f"Title: {title}")
        else: 
            raise TypeError("Title must be a string.")
    

    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
            print(f"Page Count: {page_count} pages")
        else:
            # Normally, you would use raise TypeError("page_count must be an integer")
            print("page_count must be an integer")

    
    # Test #3 of book_test.py
    def turn_page(self):
        print("Flipping the page...wow, you read fast!")




book = Book("Plunder", 340)


    
        