from constants import DEER_MESSAGE, LION_MESSAGE, BAT_MESSAGE, CAMEL_IMAGE


class Animal:
    pass


class Deer(Animal):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return DEER_MESSAGE


class Bat(Animal):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return BAT_MESSAGE


class Lion(Animal):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return LION_MESSAGE


class Camel(Animal):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return CAMEL_IMAGE
