#!/usr/bin/env python3
class Book:
    def __init__(self, title=None, page_count=None):
        self._page_count = page_count
        self.title = title
        

    def get_page_count(self):
        return self._page_count

    def set_page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        else:
            self._page_count = value

    page_count = property(get_page_count, set_page_count)
    def turn_page(self):
         print("Flipping the page...wow, you read fast!")



    
        