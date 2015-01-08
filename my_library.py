#!usr/bin/env python

"""Library model

Create an instance of the Library class first, followed by
Shelf instances and then Book instances.
Classes:
Library -- a class that contains shelves and books
Shelf -- a class that contains books and belongs to a library
Book -- a class that belongs to a library and a shelf
"""

class Library(object):
    """Library class
    
    A class that contains shelves and books.
    Attributes:
    num_shelves -- number of shelves in the library
    books -- list containing Book objects
    Methods:
    report_books -- print the shelf's book titles
    """
    def __init__(self):
        """Create an instance of Library
        
        Input no arguments
        """
        self.num_shelves = 0
        self.books = []
        
        
    def report_books(self):
        """Print the shelf's book titles
        
        Input no arguments.
        """
        for i in xrange(len(self.books)):
            print(u"{:d} {}".format(i, self.books[i].title))
    
    
class Shelf(object):
    """Shelf class
    
    A class that contains books and belongs to a library.
    Attributes:
    library -- the library which contains the shelf
    contents -- list containing the books on the shelf
    """
    def __init__(self, library):
        """Create an instance of Shelf
        
        Positional arguments:
        library -- Library object that the shelf belongs in
        """
        self.library = library
        self.contents = []
        library.num_shelves += 1


class Book(object):
    """Book class
    
    a class that belongs to a library and a shelf.
    Attributes:
    title -- the title of the book
    shelf -- the shelf that the book sits on
    """
    def __init__(self, title, shelf):
        """Create an instance of Book
        
        Positional arguments:
        title -- the title of the book
        shelf -- the shelf that the book sits on
        """
        self.title = title.capitalize()
        self.shelf = shelf
        shelf.contents.append(self)
        shelf.library.books.append(self)
    
    
    def enshelf(self, shelf):
        """Place a book on a shelf
        
        Positional arguments:
        shelf -- the shelf that the book will sit on
        """
        if not self.shelf:
            self.shelf = shelf
            shelf.contents.append(self)
        else:
            print(u"Already on a shelf")


    def unshelf(self):
        """Remove a book from a shelf
        
        Input no arguments.
        """
        if self.shelf:
            self.shelf.contents.remove(self)
            self.shelf = None
        else:
            print(u"Already not on a shelf")


if __name__ == "__main__":
    li = Library()
    s = Shelf(li)
    assert li.num_shelves == 1
    b = Book(u"The Hunger Games", s)
    assert s.contents == [b]
    b.unshelf()
    assert b.shelf == None
    b.enshelf(s)
    assert b.shelf == s
    print(u"All tests pass")
