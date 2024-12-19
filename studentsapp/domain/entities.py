from dataclasses import dataclass


@dataclass
class Student:
    __id: int
    name: str
    grade: int

    @property
    def id(self):
        return self.__id


class Teacher:
    def __init__(self, id, name):
        self.__id = id
        self.__name = name

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name
