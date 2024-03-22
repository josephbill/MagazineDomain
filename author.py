from article import Article
class Author:
    def __init__(self, name):
        # Check if name is a valid string // must be type str and longer than o characters 
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        self._name = name
        self._articles = []  # Initialize list to store articles

    #  this ensures the name property cannot be changed once set for an object 
    @property
    def name(self):
        return self._name

    # returning list of all articles belonging to this author 
    def articles(self):
        return self._articles

    # returning a unique list of magazine which the author has contributed to. 
    def magazines(self):
        # Collect unique magazines from articles
        return list(set(article.magazine for article in self._articles))

    # creating a new article instance and associating it to the author 
    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    #returning unique list of strings that belong to the author article
    def topic_areas(self):
        if not self._articles:
            return None
        return list(set(article.magazine.category for article in self._articles))
