import string


class InvalidArgumentException(Exception):
    pass


class Person():

    def __init__(self, name):
        self.name = name

    def check_name(self):
        for char in self.name:
            if char in string.ascii_letters and char.isupper():
                return True
            else:
                raise InvalidArgumentException("Invalid argument!")


p = Person('Mi?kkel')
print(p.check_name())
