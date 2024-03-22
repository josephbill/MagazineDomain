class Article:
    def __init__(self, author, magazine, title):
        # Check if title is a valid string
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        self._author = author
        self._magazine = magazine
        self._title = title

    @property
    def title(self):
        return self._title

    # return author object for the article instances
    @property
    def author(self):
        return self._author

    # return magazine object for the article instances
    @property
    def magazine(self):
        return self._magazine
    
    #add setter property to change author and magazine 
    
