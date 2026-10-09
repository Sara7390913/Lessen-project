from validation import *


class Lesson:
    def __init__(self, name, teacher, code, unit):
        self.name = name
        self.teacher = teacher
        self.code = code
        self.unit = unit

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        name_validator(value)
        self.__name = value

    @property
    def teacher(self):
        return self.__teacher

    @teacher.setter
    def teacher(self, value):
        teacher_validator(value)
        self.__teacher = value

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        code_validator(value)
        self.__code = value

    @property
    def unit(self):
        return self.__unit

    @unit.setter
    def unit(self, value):
        unit_validator(value)
        self.__unit = value
