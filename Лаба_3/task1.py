class Book:
    """ Базовый класс книги. """
    def __init__(self, name: str, author: str):
        if not isinstance(name, str):
            raise TypeError("Wrong type")
        self._name = name

        if not isinstance(author, str):
            raise TypeError("Wrong type")
        self._author = author

    @property
    def name(self):
        return self._name

    @property
    def author(self):
        return self._author

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    def __init__(self, name: str, author: str, pages: int):
        super().__init__(name=name, author=author)
        if not isinstance(pages, int):
            raise TypeError("Wrong type")
        if pages < 0:
            raise ValueError("Invalid value")
        self.pages = pages

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. {self.pages} страниц."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, pages={self.pages!r})"


class AudioBook(Book):
    def __init__(self, name: str, author: str, duration: (int, float)):
        super().__init__(name=name, author=author)
        if not isinstance(duration, (int, float)):
            raise TypeError("Wrong type")
        if duration < 0:
            raise ValueError("Invalid value")
        self.duration = duration

    def __str__(self):
        return f"Книга {self.name}. Автор {self.author}. Длительность {self.duration} минут."

    def __repr__(self):
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r}, duration={self.duration!r})"
