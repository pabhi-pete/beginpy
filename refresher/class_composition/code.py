"""
bad approched example
"""
# class BookShelf:
#     def __init__(self, quantity) -> None:
#         self.quantity = quantity
    
#     def __str__(self) -> str:
#         return f'BookShelf with {self.quantity} books.'

# shelf = BookShelf(300)
# print(shelf)

# class Book(BookShelf):
#     def __init__(self, name, quantity) -> None:
#         super().__init__(quantity)
#         self.name = name
    
#     def __str__(self):
#         return f'Book {self.name}'
"""
end of bad approched example
"""
# book = Book("Harry Potter", 120)
# print(book)

"""
New approch example
"""
class BookShelf:
    def __init__(self, *books) -> None:
        self.books = books
    
    def __str__(self) -> str:
        return f'BookShelf with {len(self.books)} books.'

class Book():
    def __init__(self, name) -> None:
        self.name = name
    
    def __str__(self):
        return f'Book {self.name}'

#### Execute Program ####
# in case we are not using inheritance, so that we use class composition instead
book1 = Book('Harry Potter')
book2 = Book('Python 101')
on_shelf = BookShelf(book1, book2)
print(on_shelf)
# on_shelf.books # wanna try to get the books list from them not sure how it works?

