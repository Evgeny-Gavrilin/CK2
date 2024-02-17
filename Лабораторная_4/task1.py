class Car:
    """Автомобиль"""
    def __init__(self, brand: str, fuel: str, top_speed: int):
        """
        Создание и подготовка к работе объекта "Автомобиль"
        :param brand: Фирма-производитель машины
        :param fuel: Тип топлива в машине
        :param top_speed: Максимальная скорость машины
        Примеры:
        >>> car = Car("Ferrari", "Petrol", 180)  # инициализация экземпляра класса
        """
        self.brand = brand
        self.fuel = fuel
        self.top_speed = top_speed

    def __str__(self):
        return f'Автомобиль марки {self.brand}. Топливо: {self.fuel}. Максимальная скорость: {self.top_speed} км/ч.'

    def __repr__(self):
        return f'{self.__class__.__name__}(brand={self.brand!r}, fuel={self.fuel!r}, top_speed={self.top_speed})'


class Passenger_Car(Car):
    """Легковой автомобиль"""
    def __init__(self, brand: str, fuel: str, top_speed: int, seats: int):
        """
        Создание и подготовка к работе объекта "Легковой автомобиль"
        :param brand: Фирма-производитель машины
        :param fuel: Тип топлива в машине
        :param top_speed: Максимальная скорость машины
        :param seats: Число сидений в машине
        Примеры:
        >>> ferrari = Passenger_Car("Ferrari", "Petrol", 180, 5)
        """
        super().__init__(brand=brand, fuel=fuel, top_speed=top_speed)
        self.seats = seats

    def __str__(self):
        return f"{super().__str__()}, Количество сидений: {self.seats}"

    def __repr__(self):
        return f'{self.__class__.__name__}(brand={self.brand!r}, fuel={self.fuel!r}, top_speed={self.top_speed},' \
               f' seats={self.seats})'

    @staticmethod
    def drive(destination: str) -> str:
        """
        Данный метод позволяет перевезти пассажирскую машину до пункта назначения
        :param destination: Пункт назначения
        :raise TypeErorr: Если тип вводимого пункта не совпадает с аннотированным, выводится ошибка
        :return: До какого пункта назначения осуществляется проезд
        Примеры:
        >>> ferrari = Passenger_Car("Ferrari", "Petrol", 180, 5)
        >>> ferrari.drive("Gatchina")
        'Driving to Gatchina'
        """
        if not isinstance(destination, str):
            raise TypeError("Вводимый пункт назначения должен быть строкой")
        return f'Driving to {destination}'

    @staticmethod
    def turn(direction: str) -> str:
        """
            Данный метод позволяет выбрать для машины нужное направление поворота
            :param direction: Направление поворота
            :raise ValueErorr: Если вводимое направление поворота неверно, выводится ошибка
            :raise TypeErorr: Если тип вводимого направления не совпадает с аннотированным, выводится ошибка
            :return: В каком направлении осуществляется поворот
            Примеры:
            >>> ferrari = Passenger_Car("Ferrari", "Petrol", 180, 5)
            >>> ferrari.turn('left')
            'Turning left'
        """
        if direction != 'left' and direction != 'right':
            raise ValueError("Неправильное направление")
        if not isinstance(direction, str):
            raise TypeError("Вводимое направление должно быть строкой")
        return f'Turning {direction}'


class Truck(Car):
    """Грузовой автомобиль"""
    def __init__(self, brand: str, fuel: str, top_speed: int, tonnage: (int, float)):
        """
        Создание и подготовка к работе объекта "Грузовой автомобиль"
        :param brand: Фирма-производитель машины
        :param fuel: Тип топлива в машине
        :param top_speed: Максимальная скорость машины
        :param tonnage: Тоннаж грузовика
        Примеры:
        >>> volvo = Truck("Volvo", "Diesel", 140, 10)
        """
        super().__init__(brand=brand, fuel=fuel, top_speed=top_speed)
        self.tonnage = tonnage

    def __str__(self):
        return f"{super().__str__()}, Тоннаж: {self.tonnage}"

    def __repr__(self):
        return f'{self.__class__.__name__}(brand={self.brand!r}, fuel={self.fuel!r}, top_speed={self.top_speed}, ' \
               f'tonnage={self.tonnage})'

    @staticmethod
    def load_cargo(cargo: str) -> str:
        """
        Данный метод позволяет загрузить грузовой автомобиль
        :param cargo: Полезный груз
        :raise TypeErorr: Если тип вводимого значения не совпадает с аннотированным, выводится ошибка
        :return: До какого пункта назначения осуществляется проезд
        Примеры:
        >>> volvo = Truck("Volvo", "Diesel", 140, 10)
        >>> volvo.load_cargo('bananas')
        'Loading bananas into the truck'
        """
        if not isinstance(cargo, str):
            raise TypeError("Вводимое значение должно быть строкой")
        return f'Loading {cargo} into the truck'

    @staticmethod
    def unload_cargo(cargo: str) -> str:
        """
        Данный метод позволяет разгрузить грузовой автомобиль
        :param cargo: Полезный груз
        :raise TypeErorr: Если тип вводимого значения не совпадает с аннотированным, выводится ошибка
        :return: Процесс разгрузки грузового автомобиля
        Примеры:
        >>> volvo = Truck("Volvo", "Diesel", 140, 10)
        >>> volvo.unload_cargo('bananas')
        'Unloading bananas from the truck'
        """
        if not isinstance(cargo, str):
            raise TypeError("Вводимое направление должно быть строкой")
        return f'Unloading {cargo} from the truck'


if __name__ == "__main__":
    pass