class Book:
    TYPES = ("hardcover", "paperback")
    
    def __init__(self, name, book_type, weight):
        self.name = name
        self.book_type = book_type
        self.weight = weight

    def __repr__(self):
        return f"<BOOK: {self.name}, {self.book_type}, weighting: {self.weight} g>"
    
    @classmethod
    def hardcover(cls, name, page_weight):
        return cls(name, cls.TYPES[0], page_weight + 100)

    @classmethod
    def paperback(cls, name, page_weight):
        return cls(name, cls.TYPES[1], page_weight)

heavy = Book.hardcover("Harry Potter", 1500)
light = Book.paperback("Python 101", 450)
original_book = Book("test_original", 'testcover', 1234)

# print(heavy)
# print(light)
print(original_book)