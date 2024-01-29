class Book:
    def __init__(self, name, author):
        self._name = name
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"{self.__class__.__name__}: {self.name} за авторством {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}('{self.name}', '{self.author}')"


class PaperBook(Book):
    def __init__(self, name, author, pages):
        super().__init__(name, author)
        self.pages = pages

    def __str__(self):
        return f"{super().__str__()}, {self.pages} Страниц"

    def __repr__(self):
        return f"{super().__repr__()}, pages={self.pages}"

    @property
    def pages(self):
        return self._pages
    @pages.setter
    def pages(self, value):
        if isinstance(value, int) and value > 0:
            self._pages = value
        else:
            raise ValueError("Число страниц должно быть положительным")


class AudioBook(Book):
    def __init__(self, name, author, duration):
        super().__init__(name, author)
        self.duration = duration

    def __str__(self):
        return f"{super().__str__()}, {self.duration} Часов"

    def __repr__(self):
        return f"{super().__repr__()}, duration={self.duration}"

    @property
    def duration(self):
        return self._duration

    @duration.setter
    def duration(self, value):
        if isinstance(value, (int, float)) and value > 0:
            self._duration = value
        else:
            raise ValueError("Длительность должна быть положительной")