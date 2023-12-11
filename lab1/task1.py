import doctest


# TODO Написать 3 класса с документацией и аннотацией типов
class Office:
    def __init__(self, area: float, floor: int, number_of_workers: int):
        """
        Создание и подготовка к работе объекта "Офис"
        :param area: Площадь офиса
        :param floor: Этаж, на котором расположен офис
        :param number_of_workers: Количество работников в офисе
        Примеры:
        >>> office = Office(80, 4, 15)  # инициализация экземпляра класса
        """
        if not isinstance(area, (int, float)):
            raise TypeError("Площадь офиса должна быть типа int или float")
        if area <= 0:
            raise ValueError("Площадь офиса должна быть положительной")
        self.area = area

        if not isinstance(floor, int):
            raise TypeError("Этаж должен быть типа int")
        if floor <= 0:
            raise ValueError("Этаж должен быть положительным")
        self.floor = floor

        if not isinstance(number_of_workers, int):
            raise TypeError("Количество работников должно быть типа int")
        if number_of_workers < 0:
            raise ValueError("Количество работников не может быть отрицательным")
        self.number_of_residents = number_of_workers

    def is_new_worker(self, num_of_chairs) -> bool:
        """
        Данный метод позволяет узнать есть ли возможность устроить на работу в офис еще одного человека
        :param num_of_chairs: Сколько стульев в офисе
        :raise ValueErorr: Если количество стульев отрицательное,выводится ошибка
        :return: Есть ли свободные стулья в офисе
        Примеры:
        >>> office = Office(80, 4, 15)
        >>> office.is_new_worker(16)
        """
        if not isinstance(num_of_chairs, int):
            raise TypeError("Количество стульев должно быть типа int или float")
        if num_of_chairs < 0:
            raise ValueError("Количество стульев не может быть отрицательным")
        ...

    def office_area_worker(self) -> float:
        """
        Данный метод позволяет рассчитать площадь офиса, расчитанная на 1 работника
        :return: Площадь, расчитанная на 1 работника
        Примеры:
        >>> office = Office(80, 4, 15)
        >>> office.office_area_worker()
        """
        ...

    def lock(self):
        """
        Данный метод позволяет закрыть офис
        Примеры:
        >>> office = Office(80, 4, 15)
        >>> office.lock()
        """
        ...


class Auto:
    def __init__(self, trademark_of_auto: str, type_auto: str, cost: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param trademark_of_auto: Марка автомобиля
        :param type_auto: Тип автомобиля
        :param cost: Стоимость автомобиля в рублях
        Примеры:
        >>> auto = Auto("Volkswagen", "Седан", 200000)  # инициализация экземпляра класса
        """
        if not isinstance(trademark_of_auto, str):
            raise TypeError("Марка автомобиля должна быть типа str")
        self.trademark_of_auto = trademark_of_auto

        if not isinstance(type_auto, str):
            raise TypeError("Тип автомобиля должен быть типа str")
        self.type_auto = type_auto

        if not isinstance(cost, (int, float)):
            raise TypeError("Стоимость авто должна быть типа int или float")
        if cost < 0:
            raise ValueError("Стоимость не может быть отрицательной")
        self.cost = cost

    def crash_test(self) -> bool:
        """
        Данный метод позволяет узнать прочный ли автомобиль
        :return: Прочный ли автомобиль
        Примеры:
        >>> auto = Auto("Volkswagen", "Седан", 200000)
        >>> auto.crash_test()
        """
        ...

    def build(self):
        """
        При помощи данного метода осуществляется сборка автомобиля
        Примеры:
        >>> auto = Auto("Volkswagen", "Седан", 200000)
        >>> auto.build()
        """
        ...

    def garage_auto(self) -> str:
        """
        Данный метод осуществляет выбор гаража для автомобиля
        :return: Гараж, в котором будет стоять автомобиль
        Примеры:
        >>> auto = Auto("Volkswagen", "Седан", 200000)
        >>> auto.garage_auto()
        """
        ...


class Language:
    def __init__(self, name: str, country: str, number_of_native_speakers: int):
        """
        Создание и подготовка к работе объекта "Язык"
        :param name: Название языка
        :param country: Страна, в котрой разговаривают на данном языке
        :param number_of_native_speakers: Количество носителей языка
        Примеры:
        >>> language = Language("Russian", "Russia", 258000000)  # инициализация экземпляра класса
        """
        if not isinstance(name, str):
            raise TypeError("Название языка должно быть типа str")
        self.name = name

        if not isinstance(country, str):
            raise TypeError("Страна должна быть типа str")
        self.country = country

        if not isinstance(number_of_native_speakers, int):
            raise TypeError("Число носителей должно быть типа int")
        if number_of_native_speakers <= 0:
            raise ValueError("Число носителей должно быть положительным")
        self.number_of_native_speakers = number_of_native_speakers

    def rewrite(self, new_language: str) -> str:
        """
        Данный метод позволяет перевести слово на другой язык
        :param new_language: Новый язык
        :raise TypeError: Если введен несуществующий язык , выводится ошибка
        :return: Переведенное слово
        Примеры:
        >>> language = Language("Russian", "Russia", 258000000)
        >>> language.rewrite("English")
        """
        if not isinstance(new_language, str):
            raise TypeError("Новый язык должен быть типа str")
        ...

    def write(self):
        """
        Данный метод позволяет написать любое слово на данном языке
        Примеры:
        >>> language = Language("Russian", "Russia", 258000000)
        >>> language.write()
        """
        ...

    def count_letters(self) -> int:
        """
        Высчитывает количество букв в алфавите
        :return: Количество букв в алфавите
        Примеры:
        >>> language = Language("Russian", "Russia", 258000000)  # инициализация экземпляра класса
        >>> language.count_letters()
        """
        ...


if __name__ == "__main__":
    doctest.testmod()  # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass

